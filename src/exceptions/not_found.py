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


class MatrixSuiteNotFoundError(NotFoundError):
    """Matrix suite not found error."""

    def __init__(
        self,
        message: str = "Matrix suite not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class SimulacrumNotFoundError(NotFoundError):
    """Simulacrum not found error."""

    def __init__(
        self,
        message: str = "Simulacrum not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class WeaponNotFoundError(NotFoundError):
    """Weapon not found error."""

    def __init__(
        self,
        message: str = "Weapon not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class GiftNotFoundError(NotFoundError):
    """Gift not found error."""

    def __init__(
        self,
        message: str = "Gift not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class MountNotFoundError(NotFoundError):
    """Mount not found error."""

    def __init__(
        self,
        message: str = "Mount not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class BannerNotFoundError(NotFoundError):
    """Banner not found error."""

    def __init__(
        self,
        message: str = "Banner not found.",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)
