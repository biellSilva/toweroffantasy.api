import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.relics import Relic
from src.enums import LANGS_GLOBAL_ENUM
from src.infra.models.relics import RawRelic
from src.infra.repository.helpers.relics import (
    ignore_relic,
    relic_advanc_rework,
    sort_relics,
)


class RelicsGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Relic]] = {}

    async def find_by_id(
        self, id: str, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> Relic | None:
        if lang_cache := self.__cache.get(lang):
            if relic := lang_cache.get(id):
                return relic
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_GLOBAL_ENUM, *args: Any, **kwargs: Any
    ) -> list[Relic]:
        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:

        if lang not in self.__cache or len(self.__cache[lang]) != len(lang):
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "relics.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, RawRelic] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            if ignore_relic(value_dict):
                continue

            value_dict["advancements"] = relic_advanc_rework(value_dict["advancement"])

            self.__cache[lang].update(
                {key_id.lower(): Relic(**value_dict)}  # type: ignore
            )

        self.__cache[lang] = sort_relics(self.__cache[lang])
