from typing import Any

from src.exceptions.base import ApiError


class NotFoundError(ApiError):
    """Not found error."""

    def __init__(
        self,
        message: str = "Resource not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, status_code=404, **metadata)


class UserNotFoundError(NotFoundError):
    """User not found error."""

    def __init__(
        self,
        message: str = "User not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class MatriceNotFoundError(NotFoundError):
    """Matrice not found error."""

    def __init__(
        self,
        message: str = "Matrice not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)
