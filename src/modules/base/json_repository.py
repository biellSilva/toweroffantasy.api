from json import loads
from typing import Any

import aiofiles

from src.modules.base.cache import RedisCache


class JsonRepository:
    def __init__(self, name: str) -> None:
        self._name = name
        self._cache = RedisCache(name=self._name)

    async def _loads_json(self, *, lang: str) -> None:
        """Load all items from the database."""

        async with aiofiles.open(f"src/database/{lang}/{self._name}.json") as file:
            data = loads(await file.read())

        await self._cache.set_values(lang=lang, value_dict=data)

    async def get_id(self, *, lang: str, _id: str) -> dict[str, Any] | None:
        """Get a item by id."""
        cache = await self._cache.get(lang=lang, key=_id)

        if not cache:
            await self._loads_json(lang=lang)

        return await self._cache.get(lang=lang, key=_id)

    async def get_all(self, *, lang: str) -> list[dict[str, Any]]:
        """Get all items."""

        cache = await self._cache.get_all(lang=lang)

        if not cache:
            await self._loads_json(lang=lang)

        return list((await self._cache.get_all(lang=lang)).values())
