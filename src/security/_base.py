from typing import TYPE_CHECKING

from fastapi import Request
from fastapi.security import APIKeyHeader

from src.core.crypt import CryptHelper
from src.exceptions.unauthorized import (
    MissingTokenError,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.exceptions.base import ApiError


class BaseSecurityScheme(APIKeyHeader):
    """Base security scheme."""

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
        self._checks: list[tuple[Callable[..., bool], ApiError | type[ApiError]]] = []

    def _get_token(self, request: Request) -> str:
        """Get token from request."""
        if token := request.headers.get(self.model.name):
            return token.replace("Bearer ", "", 1)
        raise MissingTokenError
