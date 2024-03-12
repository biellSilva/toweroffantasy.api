import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.mounts import Mount
from src.enums import LANGS_GLOBAL_ENUM
from src.infra.models.mounts import RawMount
from src.infra.repository.helpers.mounts import ignore_mounts, sort_mounts


class MountsGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Mount]] = {}

    async def find_by_id(
        self,
        id: str,
        lang: LANGS_GLOBAL_ENUM,
    ) -> Mount | None:
        if lang_cache := self.__cache.get(lang):
            if relic := lang_cache.get(id):
                return relic
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> list[Mount]:
        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:

        if lang not in self.__cache or len(self.__cache[lang]) != len(lang):
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "mount.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, RawMount] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            if ignore_mounts(value_dict):
                continue

            self.__cache[lang].update(
                {key_id.lower(): Mount(**value_dict)}  # type: ignore
            )

        self.__cache[lang] = sort_mounts(self.__cache[lang])
