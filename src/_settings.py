from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ("config",)


class _BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None, case_sensitive=False)

    ENV: Literal["prod", "dev", "test"] = "dev"

    PROJECT_NAME: str = "Tower of Fantasy API"

    DB_URL: str

    JWT_SECRET: str = "secret"

    EMAIL_MIN_LENGTH: int = 4
    EMAIL_MAX_LENGTH: int = 256
    EMAIL_REGEX: str = r"^(?=.{4,256}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    PASSWORD_MIN_LENGTH: int = 8
    PASSWORD_MAX_LENGTH: int = 256
    PASSWORD_SPECIAL_CHARS: str = "@$!%*?&"
    PASSWORD_REGEX: str = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,256}$"
    )

    USERNAME_MIN_LENGTH: int = 4
    USERNAME_MAX_LENGTH: int = 30
    USERNAME_SPECIAL_CHARS: str = "_."
    USERNAME_REGEX: str = r"^[a-zA-Z0-9_\.]{4,30}$"


config = _BaseSettings()  # type: ignore[call-arg]
