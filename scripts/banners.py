import json
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from pydantic import BaseModel, field_validator


class ExportBanner(BaseModel):
    link: str
    start_at: datetime
    end_at: datetime
    imitation_id: str
    weapon_id: str
    suit_id: str
    limited_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool


class Banner(BaseModel):
    simulacrum: str
    start: datetime
    end: datetime
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool
    no_weapon: bool
    imitation_id: str
    weapon_id: str
    matrix_id: str

    @field_validator("start", "end", mode="before")
    @classmethod
    def check_dates(cls, value: str) -> datetime:
        if ":" not in value:
            return (
                datetime.strptime(value, "%Y/%m/%d")
                .replace(
                    tzinfo=ZoneInfo("UTC"),
                )
                .replace(hour=0, minute=0, second=0)
            )
        return (
            datetime.strptime(value, "%Y/%m/%d %H:%M")
            .replace(
                tzinfo=ZoneInfo("UTC"),
            )
            .replace(second=0)
        )

    @field_validator("matrix_id", mode="before")
    @classmethod
    def check_ids(cls, value: str) -> str:
        return (
            value.replace("matrix_", "suit_").replace("ssr", "SSR").replace("sr", "SR")
        )


def load_data(path: str | Path) -> list[Banner]:
    if isinstance(path, str):
        path = Path(path)

    return [
        Banner(**banner) for banner in json.loads(path.read_bytes().decode("utf-8"))
    ]


def fix_imitations_ids(banners: list[Banner]) -> None:
    simulacras: dict[str, dict[str, Any]] = json.loads(
        Path("src/database/simulacra.json").read_bytes().decode("utf-8"),
    )

    def find_imitation_id(imitation_id: str) -> str:
        for simulacrum in simulacras.values():
            if simulacrum["id"].lower() == imitation_id.lower():
                return simulacrum["id"]

        msg = f"Imitation ID {imitation_id} not found."

        raise ValueError(msg)

    for banner in banners:
        banner.imitation_id = find_imitation_id(banner.imitation_id)


def fix_weapons_ids(banners: list[Banner]) -> None:
    weapons: dict[str, dict[str, Any]] = json.loads(
        Path("src/database/weapons.json").read_bytes().decode("utf-8"),
    )

    def find_weapon_id(weapon_id: str) -> str:
        for weapon in weapons.values():
            if weapon["id"].lower() == weapon_id.lower():
                return weapon["id"]

        msg = f"Weapon ID {weapon_id} not found."

        raise ValueError(msg)

    for banner in banners:
        banner.weapon_id = find_weapon_id(banner.weapon_id)


def fix_suits_ids(banners: list[Banner]) -> None:
    suits: dict[str, dict[str, Any]] = json.loads(
        Path("src/database/matrices.json").read_bytes().decode("utf-8"),
    )

    def find_suit_id(suit_id: str) -> str:
        for suit in suits.values():
            if suit["id"].lower() == suit_id.lower():
                return suit["id"]

        msg = f"Suit ID {suit_id} not found."

        raise ValueError(msg)

    for banner in banners:
        banner.matrix_id = find_suit_id(banner.matrix_id)


async def main() -> None:
    from prisma import Prisma
    from prisma.types import BannerCreateInput

    client = Prisma()
    await client.connect()

    banners = load_data("banners.json")

    fix_imitations_ids(banners)
    fix_weapons_ids(banners)
    fix_suits_ids(banners)

    print(f"Loaded {len(banners)} banners.")  # noqa: T201

    for banner in banners:
        await client.banner.create(
            data=BannerCreateInput(
                link=banner.details_link,
                start_at=banner.start,
                end_at=banner.end,
                imitation_id=banner.imitation_id,
                weapon_id=banner.weapon_id,
                suit_id=banner.matrix_id,
                limited_only=banner.limited_banner_only,
                is_rerun=banner.is_rerun,
                final_rerun=banner.final_rerun,
                is_collab=banner.is_collab,
            ),
        )

    print("All banners created successfully.")  # noqa: T201


def main2() -> None:
    banners = load_data("banners.json")

    fix_imitations_ids(banners)
    fix_weapons_ids(banners)
    fix_suits_ids(banners)

    print(f"Loaded {len(banners)} banners.")  # noqa: T201

    Path("banners_export.json").write_text(
        json.dumps(
            [
                ExportBanner(
                    link=banner.details_link,
                    start_at=banner.start,
                    end_at=banner.end,
                    imitation_id=banner.imitation_id,
                    weapon_id=banner.weapon_id,
                    suit_id=banner.matrix_id,
                    limited_only=banner.limited_banner_only,
                    is_rerun=banner.is_rerun,
                    final_rerun=banner.final_rerun,
                    is_collab=banner.is_collab,
                ).model_dump(mode="json")
                for banner in banners
            ],
            indent=2,
        ),
    )

    print("All banners created successfully.")  # noqa: T201


if __name__ == "__main__":
    main2()
