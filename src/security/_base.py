from typing import TYPE_CHECKING

from fastapi import Request
from fastapi.security import APIKeyHeader
from jwt import DecodeError, ExpiredSignatureError
from pydantic import ValidationError

from src.core.crypt import CryptHelper
from src.exceptions.unauthorized import (
    ExpiredTokenError,
    InvalidTokenError,
    MissingTokenError,
)
from src.modules.auth.dtos import Payload
from src.modules.users.repository import UserRepository

if TYPE_CHECKING:
    from collections.abc import Callable

    from prisma.models import User

    from src.exceptions.base import ApiError


class BaseSecurityScheme(APIKeyHeader):
    """Base security scheme."""

    _crypt_helper = CryptHelper()
    _user_repo = UserRepository()

    def __init__(
        self,
        *,
        name: str = "Authorization",
        scheme_name: str = "Authorization",
        description: str = "Bearer token",
        auto_error: bool = False,
    ) -> None:
        super().__init__(
            name=name,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )
        self._checks: list[
            tuple[Callable[[User], bool], ApiError | type[ApiError]]
        ] = []

    def _get_token(self, request: Request) -> str:
        """Get token from request."""
        if token := request.headers.get(self.model.name):
            return token.replace("Bearer ", "", 1)
        raise MissingTokenError

    async def _get_user(self, payload: Payload) -> "User | None":
        """Get user from payload."""
        return await self._user_repo.get_user_by_id(payload.id)

    async def _validate(self, request: Request) -> Payload:
        """Validate token."""
        token = self._get_token(request)
        try:
            payload = Payload(**self._crypt_helper.decode_access(token))
        except (ValidationError, DecodeError):
            raise InvalidTokenError from None

        except ExpiredSignatureError:
            raise ExpiredTokenError from None

        user = await self._get_user(payload)

        if not user:
            raise InvalidTokenError

        for check, err in self._checks:
            if not check(user):
                raise err

        request.state.user = payload
        return payload

    async def __call__(self, request: Request) -> Payload:  # type: ignore
        """Check authorization header."""
        return await self._validate(request)
