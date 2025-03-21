from typing import Annotated

from fastapi import APIRouter, Path, Security

from src.core.docs import generate_docs
from src.modules.auth.dtos import Payload
from src.modules.users.dtos import User, UserMe
from src.modules.users.repository import UserRepository
from src.modules.users.service import UserService
from src.security.auth import AuthSecurity

router = APIRouter(prefix="/users", tags=["users"])

SERVICE = UserService(UserRepository())


@router.get(path="/@me", responses=generate_docs(auth=True))
async def get_user_me(user: Annotated[Payload, Security(AuthSecurity())]) -> UserMe:
    return await SERVICE.get_user_me(user_id=user.id)


@router.get(path="/{user_id}")
async def get_user_by_id(user_id: Annotated[int, Path()]) -> User:
    """Get a user by ID."""
    return await SERVICE.get_user_by_id(user_id)
