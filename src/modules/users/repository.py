from typing import TYPE_CHECKING

from src.context.prisma_conn import PrismaContext

if TYPE_CHECKING:
    from prisma.models import User


class UserRepository:
    """UserTable repository."""

    def __init__(self) -> None:
        self._client = PrismaContext.get_client()

    async def get_user_by_id(self, user_id: int) -> "User | None":
        """Get a user by ID."""

        return await self._client.user.find_first(where={"id": user_id})
