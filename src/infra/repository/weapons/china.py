import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.weapons import Weapon
from src.enums import LANGS_CHINA_ENUM
from src.infra.models.weapons import RawWeapon
from src.infra.models.weapons._helpers.weapon_upgrade import RawWeaponUpgrade
from src.infra.repository.helpers.weapons import (
    shatter_or_charge_setter,
    sort_weapons,
    weapon_convert_stat,
    weapon_fix_minor_issues,
    weapon_skill_values,
    weapon_upgrade_mats,
)
from src.infra.repository.items.china import ItemsChinaRepository


class WeaponsChinaRepository:
    __cache: dict[LANGS_CHINA_ENUM, dict[str, Weapon]] = {}

    __ITEM_REPO = ItemsChinaRepository()

    __WEAPON_MATS: dict[str, list[list[RawWeaponUpgrade]]] = json.loads(
        Path("src/infra/database/china/weaponUpgrade.json").read_bytes()
    )

    __WEAPON_EXP_REQUIRED_LEVELS: dict[str, list[int]] = {
        str(k).lower().rsplit("_", 1)[0]: v
        for k, v in dict(
            json.loads(Path("src/infra/database/china/weaponExp.json").read_bytes())
        ).items()
    }

    __DESC_VALUES: dict[str, list[float]] = json.loads(
        Path("src/infra/database/china/weaponskillnumbers.json").read_bytes()
    )

    async def find_by_id(
        self, id: str, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> Weapon | None:
        if cached_lang := self.__cache.get(lang):
            if weapon := cached_lang.get(id):
                return weapon
            return None

        await self.load_data(lang=lang)

        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> list[Weapon]:

        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_CHINA_ENUM) -> None:

        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/china", lang, "weapons.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, RawWeapon] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            print(key_id)

            value_dict = weapon_fix_minor_issues(dict_=value_dict)

            assert isinstance(value_dict["attributes"][0]["shatter"], (float, int))
            assert isinstance(value_dict["attributes"][0]["charge"], (float, int))

            value_dict["shatter"] = shatter_or_charge_setter(
                value_dict["attributes"][0]["shatter"]
            )
            value_dict["charge"] = shatter_or_charge_setter(
                value_dict["attributes"][0]["charge"]
            )

            value_dict["weaponAdvancements"] = [  # type: ignore
                {
                    "description": advanc.get("description"),
                    "shatter": shatter_or_charge_setter(
                        value_dict["attributes"][ind]["shatter"]
                    ),
                    "charge": shatter_or_charge_setter(
                        value_dict["attributes"][ind]["charge"]
                    ),
                    "multiplier": advanc["multiplier"],
                    "need": advanc["need"],
                }
                for ind, advanc in enumerate(value_dict["advancements"], start=1)
            ]

            value_dict["stats_att"] = weapon_convert_stat(dict_=value_dict)

            if len(value_dict["advancements"]) == 7:
                value_dict["advancements"].pop()

            value_dict = await weapon_upgrade_mats(
                value_dict,
                lang,
                self.__WEAPON_MATS,
                self.__WEAPON_EXP_REQUIRED_LEVELS,
                self.__ITEM_REPO,
            )

            value_dict = weapon_skill_values(value_dict, self.__DESC_VALUES)

            value_dict["fashion"] = [fashion["weapon"] for fashion in value_dict.get("fashion", [])]  # type: ignore

            self.__cache[lang].update(
                {key_id.lower(): Weapon(**value_dict)}  # type: ignore
            )

        self.__cache[lang] = sort_weapons(self.__cache[lang])
