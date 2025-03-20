# type: ignore

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from pydantic import BaseModel, field_validator


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


def load_data(path: str | Path) -> list[Banner]:
    if isinstance(path, str):
        path = Path(path)

    return [
        Banner(**banner) for banner in json.loads(path.read_bytes().decode("utf-8"))
    ]


def main() -> None:
    banners = load_data("banners.json")

    print(f"Loaded {len(banners)} banners.")  # noqa: T201

    for ind, banner in enumerate(banners):
        _data = {
            "object_id": banner.imitation_id,
            "start_at": banner.start.isoformat(),
            "end_at": banner.end.isoformat(),
            "link": banner.details_link,
            "limited_only": banner.limited_banner_only,
            "is_rerun": banner.is_rerun,
            "is_collab": banner.is_collab,
            "final_rerun": banner.final_rerun,
        }

        resp = requests.post(
            "http://localhost:8000/banners",
            json=_data,
            timeout=5,
        )
        resp.raise_for_status()

        _data["object_id"] = banner.weapon_id

        resp = requests.post(
            "http://localhost:8000/banners",
            json=_data,
            timeout=5,
        )
        resp.raise_for_status()

        _data["object_id"] = banner.matrix_id

        resp = requests.post(
            "http://localhost:8000/banners",
            json=_data,
            timeout=5,
        )
        resp.raise_for_status()

        print(f"Banner {ind + 1} created successfully.")  # noqa: T201

    print("All banners created successfully.")  # noqa: T201


if __name__ == "__main__":
    main()
