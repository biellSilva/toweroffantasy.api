import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.researchs import Research
from src.enums import LANGS_GLOBAL_ENUM


class ResearchsGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Research]] = {}

    async def find_by_id(
        self, id: str, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> Research | None:
        if lang_cache := self.__cache.get(lang):
            if data := lang_cache.get(id):
                return data
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> list[Research]:
        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:

        if lang not in self.__cache or len(self.__cache[lang]) != len(lang):
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "research.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, dict[str, Any]] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            for material in value_dict.get("researchMats", []):
                material.update(material.get("item", {}))

            for material in value_dict.get("rewards", []):
                material.update(material.get("item", {}))

            self.__cache[lang].update({key_id.lower(): Research(**value_dict)})
