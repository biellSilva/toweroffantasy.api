import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataNotFoundErr
from src.enums import LANGS_GLOBAL_ENUM
from src.infra.models.servants import SmartServant


class SmartServantsGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, SmartServant]] = {}

    async def find_by_id(
        self,
        id: str,
        lang: LANGS_GLOBAL_ENUM,
    ) -> SmartServant | None:
        if lang_cache := self.__cache.get(lang):
            if relic := lang_cache.get(id):
                return relic
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(self, lang: LANGS_GLOBAL_ENUM) -> list[SmartServant]:
        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:

        if lang not in self.__cache or len(self.__cache[lang]) != len(lang):
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "pet.json")

        if not DATA_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, Any] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            self.__cache[lang].update({key_id.lower(): SmartServant(**value_dict)})  # type: ignore