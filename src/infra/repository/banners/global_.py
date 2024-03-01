import json
from pathlib import Path

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.banner import Banner
from src.infra.models.banners import RawBanner
from src.infra.models.simulacra import RawSimulacra
from src.infra.models.weapons import RawWeapon
from src.infra.repository.helpers.banners import sort_banners_without_number
from src.infra.repository.helpers.weapons import weapon_fix_minor_issues


class BannersGlobalRepository:
    __cache: list[Banner] = []

    async def find_by_id(
        self,
        id: str,
    ) -> list[Banner]:
        if not self.__cache:
            await self.load_data()

        return [
            banner
            for banner in self.__cache
            if (banner.simulacrumId and banner.simulacrumId.lower() == id.lower())
            or (banner.weaponId and banner.weaponId.lower() == id.lower())
            or (banner.matrixId and banner.matrixId.lower() == id.lower())
        ]

    async def get_all(self) -> list[Banner]:
        if not self.__cache:
            await self.load_data()

        return self.__cache

    async def load_data(self) -> None:

        DATA_PATH = Path("./src/infra/database/global", "banners_global.json")
        WEAPONS_PATH = Path("./src/infra/database/global/en/", "weapons.json")
        IMITATION_PATH = Path("./src/infra/database/global/en/", "imitations.json")

        if (
            not DATA_PATH.exists()
            or not WEAPONS_PATH.exists()
            or not IMITATION_PATH.exists()
        ):
            raise LangNotFoundErr

        DATA: list[RawBanner] = json.loads(DATA_PATH.read_bytes())
        DATA.sort(key=sort_banners_without_number)
        DATA.reverse()

        WEAPONS_DATA: dict[str, RawWeapon] = json.loads(WEAPONS_PATH.read_bytes())

        IMITATION_DATA: dict[str, RawSimulacra] = json.loads(
            IMITATION_PATH.read_bytes()
        )

        index = 1

        for value_dict in DATA:
            if (
                "imitation_id" not in value_dict
                or value_dict["imitation_id"] not in IMITATION_DATA
            ):
                continue

            value_dict["bannerNumber"] = index

            if imitation_data := IMITATION_DATA.get(value_dict["imitation_id"]):
                value_dict["rarity"] = imitation_data["rarity"]
                value_dict["simulacrumIcon"] = imitation_data["assetsA0"]["avatar"]

            if "weapon_id" in value_dict and value_dict["weapon_id"]:
                if weapon_data := WEAPONS_DATA.get(value_dict["weapon_id"]):
                    weapon_data = weapon_fix_minor_issues(weapon_data)

                    value_dict["element"] = weapon_data["element"]
                    value_dict["category"] = weapon_data["wc"]
                    value_dict["weaponIcon"] = weapon_data["assets"]["icon"]

            self.__cache.append(Banner(**value_dict))  # type: ignore

            index += 1

        self.__cache.reverse()
