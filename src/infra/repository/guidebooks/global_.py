import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.guidebook import GuideBook
from src.enums import LANGS_GLOBAL_ENUM


class GuidebooksGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, GuideBook]] = {}

    async def find_by_id(
        self,
        id: str,
        lang: LANGS_GLOBAL_ENUM,
    ) -> GuideBook | None:

        if cached_lang := self.__cache.get(lang):
            if guide := cached_lang.get(id):
                return guide
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(self, lang: LANGS_GLOBAL_ENUM) -> list[GuideBook]:
        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:
        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "guidebook.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, dict[str, Any]] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            if value_dict.get("id", None):
                self.__cache[lang].update({key_id.lower(): GuideBook(**value_dict)})
            else:
                self.__cache[lang].update(
                    {key_id.lower(): GuideBook(**value_dict, id=key_id)}
                )
