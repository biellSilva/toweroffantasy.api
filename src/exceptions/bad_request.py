from typing import Any

from src._settings import config
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
        super().__init__(
            message=message,
            pattern=config.EMAIL_REGEX,
            min_len=config.EMAIL_MIN_LENGTH,
            max_len=config.EMAIL_MAX_LENGTH,
            **metadata,
        )


class InvalidPasswordError(BadRequestError):
    def __init__(
        self,
        message: str = "Invalid password",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(
            message=message,
            pattern=config.PASSWORD_REGEX,
            special_chars=config.PASSWORD_SPECIAL_CHARS,
            min_len=config.PASSWORD_MIN_LENGTH,
            max_len=config.PASSWORD_MAX_LENGTH,
            **metadata,
        )


class InvalidUsernameError(BadRequestError):
    def __init__(
        self,
        message: str = "Invalid username",
        **metadata: str | float | dict[str, Any] | list[Any],
    ) -> None:
        super().__init__(
            message=message,
            pattern=config.USERNAME_REGEX,
            special_chars=config.USERNAME_SPECIAL_CHARS,
            min_len=config.USERNAME_MIN_LENGTH,
            max_len=config.USERNAME_MAX_LENGTH,
            **metadata,
        )


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
