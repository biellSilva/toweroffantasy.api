from typing import TYPE_CHECKING

from jwt import DecodeError, ExpiredSignatureError
from pydantic import ValidationError

from src._settings import config
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
    Payload,
    RegisterParams,
)
from src.modules.users.dtos import User
from src.validators.regex import RegexValidator

if TYPE_CHECKING:
    from src.core.crypt import CryptHelper
    from src.modules.auth.repository import AuthRepository


class AuthService:
    def __init__(
        self,
        auth_repository: "AuthRepository",
        crypt_helper: "CryptHelper",
    ) -> None:
        self.repository = auth_repository
        self.crypt_helper = crypt_helper

    async def login(self, params: LoginParams) -> LoginResponse:
        """Login with email and password."""
        user = await self.repository.get_user(email=params.email)
        if not user:
            raise EmailOrPasswordError

        if not self.crypt_helper.check_password(params.password, user.password):
            raise EmailOrPasswordError

        access_token, access_timestamp, refresh_token = self.crypt_helper.encode(
            Payload(**user.model_dump()).model_dump(),
        )

        return LoginResponse(
            user=User(**user.model_dump()),
            access_token=access_token,
            access_expire=access_timestamp,
            refresh_token=refresh_token,
        )

    async def register(self, params: RegisterParams) -> LoginResponse:
        """Register a new user."""

        if _user := await self.repository.get_user_by_email_or_username(
            params.email,
            params.username,
        ):
            if _user.email == params.email:
                raise EmailOrPasswordError

            if _user.username == params.username:
                raise UsernameAlreadyExistsError

        RegexValidator(
            string=params.username,
            regex=config.USERNAME_REGEX,
            exception=InvalidUsernameError,
        )

        RegexValidator(
            string=params.email,
            regex=config.EMAIL_REGEX,
            exception=InvalidEmailError,
        )

        RegexValidator(
            string=params.password,
            regex=config.PASSWORD_REGEX,
            exception=InvalidPasswordError,
        )

        params.password = self.crypt_helper.hash_password(params.password)

        user = await self.repository.create_user(params)

        access_token, access_expire, refresh_token = self.crypt_helper.encode(
            Payload(**user.model_dump()).model_dump(),
        )

        return LoginResponse(
            user=User(**user.model_dump()),
            access_token=access_token,
            access_expire=access_expire,
            refresh_token=refresh_token,
        )

    async def change_password(self, user_id: int, params: ChangePasswordParams) -> User:
        """Change the password of the current user."""
        user = await self.repository.get_user(id=user_id)
        if not user:
            raise UserNotFoundError

        if self.crypt_helper.check_password(params.new_password, user.password):
            raise PasswordsDoNotMatchError

        old_hashes = await self.repository.get_old_passwords(user_id=user.id)

        for old_hash in old_hashes:
            if self.crypt_helper.check_password(params.new_password, old_hash.password):
                raise PasswordAlreadyUsedError

        RegexValidator(
            string=params.new_password,
            regex=config.PASSWORD_REGEX,
            exception=InvalidPasswordError,
        )

        new_password = self.crypt_helper.hash_password(params.new_password)

        user = await self.repository.update_user_password(user, new_password)
        return User(**user.__dict__)

    async def check_access_token(self, token: str) -> None:
        try:
            self.crypt_helper.decode_access(token)
        except (ValidationError, DecodeError):
            raise InvalidTokenError from None

        except ExpiredSignatureError:
            raise ExpiredTokenError from None
