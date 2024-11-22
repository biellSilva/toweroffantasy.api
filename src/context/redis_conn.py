from typing import ClassVar

import redis.asyncio as redis

from src._settings import config


class RedisConnection:
    _pool: redis.ConnectionPool | None = None
    _connections: ClassVar[list[redis.Redis]] = []

    @staticmethod
    def get_pool() -> redis.ConnectionPool:
        if RedisConnection._pool is None:
            return RedisConnection.create_pool()
        return RedisConnection._pool

    @staticmethod
    def create_pool() -> redis.ConnectionPool:
        if RedisConnection._pool is not None:
            err_msg = (
                "ConnectionPool is already set. "
                "Use `RedisConnection.get_pool()` to get the pool."
            )
            raise ValueError(err_msg)

        RedisConnection._pool = redis.ConnectionPool.from_url(url=config.REDIS_URL)  # type: ignore[assignment]
        return RedisConnection._pool

    @staticmethod
    def get_conn() -> redis.Redis:
        client = redis.Redis(connection_pool=RedisConnection.get_pool())
        RedisConnection._connections.append(client)
        return client

    @staticmethod
    async def close_all_connections() -> None:
        for conn in RedisConnection._connections:
            await conn.close()
        RedisConnection._connections.clear()
