import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataNotFoundErr
from src.domain.models.food import Food

from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class FoodRepository:
    cache: dict[
        VERSIONS_ENUM,
        dict[LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM, dict[str, Food]],
    ] = {}

    async def find_by_id(
        self,
        id: str,
        version: VERSIONS_ENUM,
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    ) -> Food | None:

        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                if food := cached_lang.get(id):
                    return food
                return None

        await self.load_data(version=version, lang=lang)

        return await self.find_by_id(id=id, version=version, lang=lang)

    async def get_all(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> list[Food]:
        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                return list(cached_lang.values())

        await self.load_data(version=version, lang=lang)

        return await self.get_all(version=version, lang=lang)

    async def load_data(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> None:
        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        DATA_PATH = Path("./src/infra/database", version, lang, "food.json")

        if not DATA_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, Any] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            if value_dict.get("id", None):
                self.cache[version][lang].update({key_id.lower(): Food(**value_dict)})
            else:
                self.cache[version][lang].update(
                    {key_id.lower(): Food(**value_dict, id=key_id)}
                )
