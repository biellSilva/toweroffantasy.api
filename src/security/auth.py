from typing import Literal

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


class AuthSecurity(APIKeyHeader):
    """Authorization security scheme."""

    _crypt_helper = CryptHelper()

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

    def _get_token(self, request: Request) -> str:
        """Get token from request."""
        if token := request.headers.get(self.model.name):
            return token
        raise MissingTokenError

    async def _validate(self, request: Request) -> Literal[True]:
        """Validate token."""
        token = self._get_token(request)
        try:
            payload = Payload(**self._crypt_helper.decode_access(token))
        except (ValidationError, DecodeError):
            raise InvalidTokenError from None

        except ExpiredSignatureError:
            raise ExpiredTokenError from None

        request.state.user = payload
        return True

    async def __call__(self, request: Request) -> None:
        """Check authorization header."""
        await self._validate(request)
