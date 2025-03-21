from typing import Annotated

from fastapi import APIRouter, Body, Request, Security, status

from src.core.crypt import CryptHelper
from src.core.docs import generate_docs
from src.exceptions.bad_request import (
    InvalidEmailError,
    InvalidPasswordError,
    InvalidUsernameError,
    PasswordsDoNotMatchError,
)
from src.exceptions.conflict import UsernameAlreadyExistsError
from src.exceptions.not_found import UserNotFoundError
from src.exceptions.unauthorized import EmailOrPasswordError
from src.modules.auth.dtos import (
    ChangePasswordParams,
    LoginParams,
    LoginResponse,
    Payload,
    RegisterParams,
)
from src.modules.auth.repository import AuthRepository
from src.modules.auth.service import AuthService
from src.security.auth import AuthSecurity

router = APIRouter(prefix="/auth", tags=["auth"])

SERVICE = AuthService(AuthRepository(), CryptHelper())


@router.post(path="/login", responses=generate_docs(EmailOrPasswordError))
async def login(params: Annotated[LoginParams, Body()]) -> LoginResponse:
    """Login with email and password."""
    return await SERVICE.login(params)


@router.post(
    path="/register",
    responses=generate_docs(
        EmailOrPasswordError,
        UsernameAlreadyExistsError,
        InvalidUsernameError,
        InvalidEmailError,
        InvalidPasswordError,
    ),
)
async def register(params: Annotated[RegisterParams, Body()]) -> LoginResponse:
    """Register a new user."""
    return await SERVICE.register(params)


@router.patch(
    path="/change-password",
    responses=generate_docs(
        UserNotFoundError,
        PasswordsDoNotMatchError,
        InvalidPasswordError,
    ),
    status_code=status.HTTP_204_NO_CONTENT,
)
async def change_password(
    user: Annotated[Payload, Security(AuthSecurity())],
    params: Annotated[ChangePasswordParams, Body()],
) -> None:
    """Change the password of the current user."""
    await SERVICE.change_password(user.id, params)


@router.get("/check")
async def check_access_token(request: Request) -> None:
    """Check if the access token is valid."""
    await SERVICE.check_access_token(request)
