from json import loads

import aiofiles
from pydantic import BaseModel

from src.modules.base.cache import RedisCache


class JsonRepository[T: BaseModel, B: BaseModel]:
    def __init__(self, *, name: str, model: type[T], simple_model: type[B]) -> None:
        self._name = name
        self._model = model
        self._list_model = simple_model
        self._cache = RedisCache(name=self._name)

    async def _loads_json(self, *, lang: str) -> None:
        """Load all items from the database."""

        async with aiofiles.open(f"src/database/{lang}/{self._name}.json") as file:
            data = loads(await file.read())

        await self._cache.set_values(lang=lang, value_dict=data)

    async def get_id(self, *, lang: str, _id: str) -> T | None:
        """Get a item by id."""
        cache = await self._cache.get(lang=lang, key=_id)

        if not cache:
            await self._loads_json(lang=lang)

        if data := await self._cache.get(lang=lang, key=_id):
            return self._model(**data)
        return None

    async def get_all(self, *, lang: str) -> list[B]:
        """Get all items."""

        cache = await self._cache.get_all(lang=lang)

        if not cache:
            await self._loads_json(lang=lang)

        return [
            self._list_model(**data)
            for data in (await self._cache.get_all(lang=lang)).values()
        ]
