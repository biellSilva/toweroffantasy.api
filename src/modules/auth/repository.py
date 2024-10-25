from collections.abc import Sequence
from typing import Self

from sqlalchemy import select

from src.modules.auth.dtos import RegisterParams
from src.modules.auth.table import OldHashTable
from src.modules.base.repository import BaseRepository
from src.modules.user.dtos import UpdateUser
from src.modules.user.table import UserTable


class AuthRepository(BaseRepository):
    __instance: Self | None = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    async def create_user(self, create_user: RegisterParams) -> UserTable:
        """Create a user."""
        return await self._save(UserTable(**create_user.model_dump()))

    async def update_user(
        self,
        user: UserTable,
        update_user: UpdateUser,
    ) -> UserTable:
        """Update a user."""
        user.update(update_user)
        return await self._save(user)

    async def update_user_password(
        self,
        user: UserTable,
        new_password: str,
    ) -> UserTable:
        """Update a user's password."""
        async with self._session() as session:
            old_hash = OldHashTable(user_id=user.id, password=user.password)
            session.add(old_hash)
            user.password = new_password
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def get_user(self, **filters: str | float) -> UserTable | None:
        """Get a user by specified filters."""
        query = select(UserTable).filter_by(**filters)
        return (await self._execute_query(query)).first()

    async def get_user_by_email_or_username(
        self,
        email: str,
        username: str,
    ) -> UserTable | None:
        """Get a user by email or username."""
        query = select(UserTable).where(
            (UserTable.email == email) | (UserTable.username == username),
        )
        return (await self._execute_query(query)).first()

    async def get_old_passwords(self, user_id: int) -> Sequence[OldHashTable]:
        """Get old passwords of a user."""
        query = select(OldHashTable).where(OldHashTable.user_id == user_id)
        return (await self._execute_query(query)).all()
