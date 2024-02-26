import json
from pathlib import Path

from src.domain.errors.http import DataNotFoundErr
from src.domain.models.weapons import Weapon
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.infra.models.meta import RawMeta
from src.infra.models.weapons import RawWeapon
from src.infra.models.weapons._helpers.weapon_upgrade import RawWeaponUpgrade
from src.infra.repository.banners import BannersRepository
from src.infra.repository.helpers.weapons import (
    ignore_weapon,
    shatter_or_charge_setter,
    sort_weapons,
    weapon_convert_stat,
    weapon_fix_minor_issues,
    weapon_skill_values,
    weapon_upgrade_mats,
)
from src.infra.repository.items import ItemsRepository


class WeaponsRepository:
    __cache: dict[
        VERSIONS_ENUM,
        dict[LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM, dict[str, Weapon]],
    ] = {}

    __ITEM_REPO = ItemsRepository()

    __META_GB: dict[str, RawMeta] = json.loads(
        Path("src/infra/database/global/meta.json").read_bytes()
    )
    __WEAPON_MATS: dict[str, list[list[RawWeaponUpgrade]]] = json.loads(
        Path(f"src/infra/database/global/weaponUpgrade.json").read_bytes()
    )

    __WEAPON_EXP_REQUIRED_LEVELS: dict[str, list[int]] = {
        str(k).lower().rsplit("_", 1)[0]: v
        for k, v in dict(
            json.loads(Path(f"src/infra/database/global/weaponExp.json").read_bytes())
        ).items()
    }

    __DESC_VALUES: dict[str, list[float]] = json.loads(
        Path("src/infra/database/global/weaponskillnumbers.json").read_bytes()
    )

    __BANNERS_REPO = BannersRepository()

    async def find_by_id(
        self,
        id: str,
        version: VERSIONS_ENUM,
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    ) -> Weapon | None:
        if cached_version := self.__cache.get(version):
            if cached_lang := cached_version.get(lang):
                if weapon := cached_lang.get(id):
                    return weapon
                return None

        await self.load_data(version=version, lang=lang)

        return await self.find_by_id(id=id, version=version, lang=lang)

    async def get_all(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> list[Weapon]:
        if cached_version := self.__cache.get(version):
            if cached_lang := cached_version.get(lang):
                return list(cached_lang.values())

        await self.load_data(version=version, lang=lang)

        return await self.get_all(version=version, lang=lang)

    async def load_data(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> None:

        if version not in self.__cache:
            self.__cache.update({version: {}})

        if lang not in self.__cache[version]:
            self.__cache[version].update({lang: {}})

        DATA_PATH = Path("./src/infra/database", version, lang, "weapons.json")

        if not DATA_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, RawWeapon] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            if ignore_weapon(dict_=value_dict):
                continue

            value_dict = weapon_fix_minor_issues(dict_=value_dict)

            value_dict["banners"] = await self.__BANNERS_REPO.find_by_id(
                id=value_dict["id"]
            )

            assert isinstance(value_dict["advancements"][0]["shatter"], (float, int))
            assert isinstance(value_dict["advancements"][0]["charge"], (float, int))

            value_dict["shatter"] = shatter_or_charge_setter(
                value_dict["advancements"][0]["shatter"]
            )
            value_dict["charge"] = shatter_or_charge_setter(
                value_dict["advancements"][0]["charge"]
            )

            value_dict["advancements"] = [  # type: ignore
                {
                    "description": advanc.get("description"),
                    "shatter": shatter_or_charge_setter(advanc["shatter"]),
                    "charge": shatter_or_charge_setter(advanc["charge"]),
                    "multiplier": advanc["multiplier"],
                    "need": advanc["need"],
                }
                for advanc in value_dict["advancements"]
                if isinstance(advanc["shatter"], float)
                and isinstance(advanc["charge"], float)
            ]

            value_dict["stats_att"] = weapon_convert_stat(dict_=value_dict)

            if len(value_dict["advancements"]) == 7:
                value_dict["advancements"].pop()

            if meta := self.__META_GB.get(key_id.lower(), None):
                value_dict["meta"] = meta

            value_dict = await weapon_upgrade_mats(
                value_dict,
                version,
                lang,
                self.__WEAPON_MATS,
                self.__WEAPON_EXP_REQUIRED_LEVELS,
                self.__ITEM_REPO,
            )

            value_dict = weapon_skill_values(value_dict, self.__DESC_VALUES)

            self.__cache[version][lang].update({key_id.lower(): Weapon(**value_dict)})  # type: ignore

        self.__cache[version][lang] = sort_weapons(self.__cache[version][lang])
