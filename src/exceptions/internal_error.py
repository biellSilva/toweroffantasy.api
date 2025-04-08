from typing import Any

from src.exceptions.base import ApiError


class InternalError(ApiError):
    """Internal error class."""

    def __init__(self, message: str = "Internal Server Error", **metadata: Any) -> None:
        super().__init__(message=message, status_code=500, **metadata)


class FailedToCreateBannerError(InternalError):
    """Failed to create banner error class."""

    def __init__(
        self,
        message: str = "Failed to create banner",
        **metadata: Any,
    ) -> None:
        super().__init__(message=message, status_code=500, **metadata)
