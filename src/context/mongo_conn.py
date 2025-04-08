from typing import Self

from motor.motor_asyncio import AsyncIOMotorClient

from src._settings import config


class MongoContext:
    __instance: Self | None = None

    _client: AsyncIOMotorClient | None = None

    def __new__(cls) -> Self:
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @staticmethod
    def get_client() -> AsyncIOMotorClient:
        if MongoContext._client is None:
            return MongoContext._create_client()
        return MongoContext._client

    @staticmethod
    def _create_client() -> AsyncIOMotorClient:
        MongoContext._client = AsyncIOMotorClient(
            config.MONGO_URI,
            tz_aware=True,
            connect=True,
        )
        return MongoContext._client

    @staticmethod
    async def close_client() -> None:
        if MongoContext._client:
            MongoContext._client.close()

    @staticmethod
    async def ping() -> None:
        await MongoContext.get_client().get_database("admin").command("ping")
