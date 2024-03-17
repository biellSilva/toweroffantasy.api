import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataIncompleteErr, LangNotFoundErr
from src.domain.models.gears import Gear
from src.enums import LANGS_GLOBAL_ENUM
from src.infra.models.gears import RawGear
from src.infra.repository.helpers.gears import ignore_gears, sort_gears


class GearsGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Gear]] = {}

    async def find_by_id(
        self, id: str, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> Gear | None:
        if lang_cache := self.__cache.get(lang):
            if relic := lang_cache.get(id):
                return relic
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> list[Gear]:
        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(
        self, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> None:

        if lang not in self.__cache or len(self.__cache[lang]) != len(lang):
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "gear.json")

        BASE_STATS_PATH = Path("./src/infra/database/global", lang, "stats.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        if not BASE_STATS_PATH.exists():
            raise DataIncompleteErr

        DATA: dict[str, RawGear] = json.loads(DATA_PATH.read_bytes())

        BASE_STATS_DATA: dict[str, dict[str, Any]] = json.loads(
            BASE_STATS_PATH.read_bytes()
        )

        for key_id, value_dict in DATA.items():

            if ignore_gears(value_dict):
                continue

            for stat in value_dict["statPool"]:
                stat = stat.update(BASE_STATS_DATA[stat["PropName"]])  # type: ignore

            for stat in value_dict["baseStat"]:
                stat = stat.update(BASE_STATS_DATA[stat["PropName"]])  # type: ignore

            value_dict["props"] = [
                {"PropId": prop_id, **prop_data}
                for prop in value_dict["props"]
                for prop_id, prop_data in prop.items()
            ]

            value_dict["advancement"] = [
                [{"matAmount": mat["mat_amount"], **mat["mat_id"]}]
                for level_advance in value_dict["advancement"]
                for mat in level_advance
            ]

            self.__cache[lang].update({key_id.lower(): Gear(**value_dict)})  # type: ignore

        self.__cache[lang] = sort_gears(self.__cache[lang])
