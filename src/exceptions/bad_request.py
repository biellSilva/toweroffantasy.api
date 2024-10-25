from typing import Any

from src.exceptions.base import ApiError


class BadRequestError(ApiError):
    def __init__(
        self,
        message: str = "Bad Request",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, status_code=400, **metadata)


class InvalidEmailError(BadRequestError):
    def __init__(
        self,
        message: str = "Invalid email",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class InvalidPasswordError(BadRequestError):
    def __init__(
        self,
        message: str = "Invalid password",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class InvalidUsernameError(BadRequestError):
    def __init__(
        self,
        message: str = "Invalid username",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class PasswordsDoNotMatchError(BadRequestError):
    def __init__(
        self,
        message: str = "Passwords do not match",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)


class MissingParamsError(BadRequestError):
    def __init__(
        self,
        message: str = "Missing parameters",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(message=message, **metadata)
