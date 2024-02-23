import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataNotFoundErr
from src.domain.models.items import Item
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class ItemsRepository:
    cache: dict[
        VERSIONS_ENUM, dict[LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM, dict[str, Item]]
    ] = {}

    async def find_by_id(
        self,
        id: str,
        version: VERSIONS_ENUM,
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    ) -> Item | None:

        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                if simulacra := cached_lang.get(id):
                    return simulacra
                return None

        await self.load_data(version=version, lang=lang)

        return await self.find_by_id(id=id, version=version, lang=lang)

    async def get_all(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> list[Item]:
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

        DATA_PATH = Path("./src/infra/database", version, lang, "items.json")
        CURRENCY_PATH = Path("./src/infra/database", version, lang, "currency2.json")

        if not DATA_PATH.exists() or not CURRENCY_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, dict[str, Any]] = json.loads(DATA_PATH.read_bytes())
        CURRENCY_DATA: dict[str, dict[str, Any]] = json.loads(
            CURRENCY_PATH.read_bytes()
        )

        DATA.update(CURRENCY_DATA)

        for key_id, value_dict in DATA.items():
            if value_dict.get("id", None):
                self.cache[version][lang].update({key_id.lower(): Item(**value_dict)})
            else:
                self.cache[version][lang].update(
                    {key_id.lower(): Item(**value_dict, id=key_id)}
                )
