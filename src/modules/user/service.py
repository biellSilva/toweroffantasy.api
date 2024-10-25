from typing import TYPE_CHECKING

from src.exceptions.not_found import UserNotFoundError
from src.modules.user.dtos import User

if TYPE_CHECKING:
    from src.modules.user.repository import UserRepository


class UserService:
    """UserTable service."""

    def __init__(self, user_repository: "UserRepository") -> None:
        self.user_repository = user_repository

    async def get_user_by_id(self, user_id: int) -> User:
        """Get a user by ID."""
        user_ = await self.user_repository.get_user_by_id(user_id)
        if user_ is None:
            raise UserNotFoundError(userId=user_id)
        return User(**user_.__dict__)
