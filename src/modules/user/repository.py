from typing import Self

from sqlalchemy import select

from src.modules.base.repository import BaseRepository
from src.modules.user.table import UserTable


class UserRepository(BaseRepository):
    """UserTable repository."""

    __instance: Self | None = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    async def get_user_by_id(self, user_id: int) -> UserTable | None:
        """Get a user by ID."""

        return (
            await self._execute_query(select(UserTable).where(UserTable.id == user_id))
        ).first()

    async def get_user_by_email(self, email: str) -> UserTable | None:
        """Get a user by email."""
        return (
            await self._execute_query(select(UserTable).where(UserTable.email == email))
        ).first()

    async def get_user_by_username(self, username: str) -> UserTable | None:
        """Get a user by username."""
        return (
            await self._execute_query(
                select(UserTable).where(UserTable.username == username),
            )
        ).first()
