from typing import Annotated

from fastapi import Path, Request

from src.core.router import ApiRouter
from src.exceptions.not_found import UserNotFoundError
from src.modules.user.dtos import User
from src.modules.user.repository import UserRepository
from src.modules.user.service import UserService

router = ApiRouter(prefix="/user", tags=["user"])

SERVICE = UserService(UserRepository())


@router.get(path="/@me", response_model=User, requires_login=True)
async def get_user_me(request: Request) -> User:
    return await SERVICE.get_user_by_id(user_id=request.state.user.id)


@router.get(
    path="/{user_id}",
    response_model=User,
    exceptions=[UserNotFoundError],
)
async def get_user_by_id(
    user_id: Annotated[int, Path()],
) -> User:
    """Get a user by ID."""
    return await SERVICE.get_user_by_id(user_id)
