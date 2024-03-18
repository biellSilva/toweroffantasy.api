import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.servants import SmartServant
from src.enums import LANGS_CHINA_ENUM
from src.infra.repository.helpers.servants import sort_servants
from src.infra.repository.items.china import ItemsChinaRepository


class SmartServantsChinaRepository:
    __cache: dict[LANGS_CHINA_ENUM, dict[str, SmartServant]] = {}

    __ITEMS_REPO = ItemsChinaRepository()

    async def find_by_id(
        self, id: str, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> SmartServant | None:
        if lang_cache := self.__cache.get(lang):
            if data := lang_cache.get(id):
                return data
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> list[SmartServant]:
        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_CHINA_ENUM) -> None:

        if lang not in self.__cache or len(self.__cache[lang]) != len(lang):
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/china", lang, "pet.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, Any] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            for advancement in value_dict["advancements"]:
                for material in advancement["mats"]:
                    if item := await self.__ITEMS_REPO.find_by_id(
                        material["mat_id"].lower(), lang
                    ):
                        material.update(item.model_dump())

            self.__cache[lang].update({key_id.lower(): SmartServant(**value_dict)})

        self.__cache[lang] = sort_servants(self.__cache[lang])
