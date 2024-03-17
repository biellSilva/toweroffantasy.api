import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.items import Item
from src.enums import LANGS_CHINA_ENUM


class ItemsChinaRepository:
    __cache: dict[LANGS_CHINA_ENUM, dict[str, Item]] = {}

    async def find_by_id(
        self, id: str, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> Item | None:

        if cached_lang := self.__cache.get(lang):
            if item := cached_lang.get(id):
                return item
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> list[Item]:

        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_CHINA_ENUM) -> None:
        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/china", lang, "items.json")
        # CURRENCY_PATH = Path("./src/infra/database/china", lang, "currency2.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, dict[str, Any]] = json.loads(DATA_PATH.read_bytes())
        # CURRENCY_DATA: dict[str, dict[str, Any]] = json.loads(
        #     CURRENCY_PATH.read_bytes()
        # )

        # DATA.update(CURRENCY_DATA)

        for key_id, value_dict in DATA.items():
            if value_dict.get("id", None):
                self.__cache[lang].update({key_id.lower(): Item(**value_dict)})
            else:
                self.__cache[lang].update(
                    {key_id.lower(): Item(**value_dict, id=key_id)}
                )
