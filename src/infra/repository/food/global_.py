import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataNotFoundErr
from src.domain.models.food import Food
from src.enums import LANGS_GLOBAL_ENUM


class FoodGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Food]] = {}

    async def find_by_id(
        self,
        id: str,
        lang: LANGS_GLOBAL_ENUM,
    ) -> Food | None:

        if cached_lang := self.__cache.get(lang):
            if food := cached_lang.get(id):
                return food
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(self, lang: LANGS_GLOBAL_ENUM) -> list[Food]:

        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:
        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "food.json")

        if not DATA_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, dict[str, Any]] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            if value_dict.get("id", None):
                self.__cache[lang].update({key_id.lower(): Food(**value_dict)})
            else:
                self.__cache[lang].update(
                    {key_id.lower(): Food(**value_dict, id=key_id)}
                )
