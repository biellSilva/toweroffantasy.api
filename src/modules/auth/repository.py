from typing import TYPE_CHECKING

from src.modules.users.repository import UserRepository

if TYPE_CHECKING:
    from prisma.models import User


class AuthRepository(UserRepository):
    """Auth repository."""

    async def get_user_by_email(self, email: str) -> "User | None":
        """Get a user by email."""
        return await self._client.user.find_first(where={"email": email})

    async def get_user_by_email_or_username(
        self,
        email: str,
        username: str,
    ) -> "User | None":
        """Get a user by email or username."""
        return await self._client.user.find_first(
            where={"OR": [{"email": email}, {"username": username}]},
        )

    async def create_user(self, email: str, password: str, username: str) -> "User":
        """Create a new user."""
        return await self._client.user.create(
            data={"email": email, "password": password, "username": username},
        )

    async def update_user_password(self, user_id: int, password: str) -> "User | None":
        """Update user password."""
        return await self._client.user.update(
            where={"id": user_id},
            data={"password": password},
        )
