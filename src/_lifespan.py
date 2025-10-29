from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from src.context.mongo_conn import MongoContext
from src.context.redis_conn import RedisConnection

if TYPE_CHECKING:
    from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: "FastAPI") -> AsyncGenerator[None, None]:
    """Application lifespan event."""

    await MongoContext.ping()
    RedisConnection.get_pool()

    yield

    await MongoContext.close_client()
    await RedisConnection.close_all_connections()
