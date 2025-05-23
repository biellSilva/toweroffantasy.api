from json import dumps, loads
from typing import Any

from pydantic import BaseModel

from src._settings import config
from src.context.redis_conn import RedisConnection


class Redis:
    _client = RedisConnection.get_conn()

    def __init__(self, name: str) -> None:
        self.module = name

    async def get(self, *, lang: str, key: str) -> dict[str, Any] | None:
        """Get a value from the cache."""
        if data := await self._client.get(name=f"{self.module}:{lang}:{key}"):
            return loads(data)
        return None

    async def get_all(self, *, lang: str) -> dict[str, dict[str, Any]]:
        """Get all values from the cache."""
        keys = await self._client.keys(pattern=f"{self.module}:{lang}:*")  # type: ignore[arg-type]
        data = await self._client.mget(keys=keys)
        return {
            str(key).rsplit(":", 1)[-1]: loads(value)
            for key, value in zip(keys, data, strict=False)
        }

    async def set_all(
        self,
        *,
        lang: str,
        value_dict: dict[str, dict[str, Any] | Any],
    ) -> None:
        """Set a value in the cache."""
        for key, value in value_dict.items():
            data = value
            if isinstance(value, BaseModel):
                data = value.model_dump(mode="json")

            await self._client.set(
                name=f"{self.module}:{lang}:{key}",
                value=dumps(data),
                ex=config.CACHE_EXPIRE,
            )

    async def set_value(
        self,
        *,
        lang: str,
        key: str,
        value: dict[str, Any],
    ) -> None:
        """Set a value in the cache."""
        await self._client.set(
            name=f"{self.module}:{lang}:{key}",
            value=dumps(value),
            ex=config.CACHE_EXPIRE,
        )
