from typing import Self

from prisma import Prisma


class PrismaContext:
    __instance: Self | None = None

    _client: Prisma | None = None

    def __new__(cls) -> Self:
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @staticmethod
    def get_client() -> Prisma:
        if PrismaContext._client is None:
            return PrismaContext._create_client()
        return PrismaContext._client

    @staticmethod
    def _create_client() -> Prisma:
        if PrismaContext._client is not None:
            err_msg = (
                "Prisma client is already set. "
                "Use `PrismaContext.get_client()` to get the client."
            )
            raise ValueError(err_msg)

        PrismaContext._client = Prisma(auto_register=True)
        return PrismaContext._client

    @staticmethod
    async def connect_client() -> None:
        client = PrismaContext.get_client()
        await client.connect()

    @staticmethod
    async def disconnect_client() -> None:
        if PrismaContext._client is not None:
            await PrismaContext._client.disconnect()
            PrismaContext._client = None
