from typing import Annotated

from fastapi import Body, Request, status

from src.core.crypt import CryptHelper
from src.core.router import ApiRouter
from src.exceptions.bad_request import (
    InvalidEmailError,
    InvalidPasswordError,
    InvalidUsernameError,
    PasswordsDoNotMatchError,
)
from src.exceptions.conflict import PasswordAlreadyUsedError, UsernameAlreadyExistsError
from src.exceptions.not_found import UserNotFoundError
from src.exceptions.unauthorized import (
    EmailOrPasswordError,
    ExpiredTokenError,
    InvalidTokenError,
)
from src.modules.auth.dtos import (
    ChangePasswordParams,
    LoginParams,
    LoginResponse,
    RegisterParams,
)
from src.modules.auth.repository import AuthRepository
from src.modules.auth.service import AuthService

router = ApiRouter(prefix="/auth", tags=["auth"])

SERVICE = AuthService(AuthRepository(), CryptHelper())


@router.post(
    path="/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
    exceptions=[EmailOrPasswordError],
)
async def login(params: Annotated[LoginParams, Body()]) -> LoginResponse:
    """Login with email and password."""
    return await SERVICE.login(params)


@router.post(
    path="/register",
    response_model=LoginResponse,
    status_code=status.HTTP_201_CREATED,
    exceptions=[
        EmailOrPasswordError,
        InvalidUsernameError,
        InvalidEmailError,
        InvalidPasswordError,
        UsernameAlreadyExistsError,
    ],
)
async def register(params: Annotated[RegisterParams, Body()]) -> LoginResponse:
    """Register a new user."""
    return await SERVICE.register(params)


@router.patch(
    path="/change-password",
    requires_login=True,
    status_code=status.HTTP_204_NO_CONTENT,
    exceptions=[
        UserNotFoundError,
        PasswordAlreadyUsedError,
        PasswordsDoNotMatchError,
        InvalidPasswordError,
    ],
)
async def change_password(
    request: Request,
    params: Annotated[ChangePasswordParams, Body()],
) -> None:
    """Change the password of the current user."""
    await SERVICE.change_password(request.state.user.id, params)


@router.get(
    "/check",
    status_code=status.HTTP_204_NO_CONTENT,
    exceptions=[InvalidTokenError, ExpiredTokenError],
    requires_login=True,
)
async def check_access_token(request: Request) -> None:
    """Check if the access token is valid."""
    await SERVICE.check_access_token(request)
