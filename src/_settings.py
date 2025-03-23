from datetime import datetime
from typing import Literal
from zoneinfo import ZoneInfo

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ("config",)


class _BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None, case_sensitive=False)

    ENV: Literal["prod", "dev", "test"] = "dev"

    PROJECT_NAME: str = "Tower of Fantasy API"

    DB_URL: str
    REDIS_URL: str

    ACCESS_SECRET: str = "secret"
    ACCESS_EXPIRE: int = 60 * 15

    REFRESH_SECRET: str = "secret"
    REFRESH_EXPIRE: int = 60 * 60 * 24

    CACHE_EXPIRE: int = 60 * 60

    ASSETS_PREFIX: str = "https://raw.githubusercontent.com/biellSilva/toweroffantasy.images/refs/heads/main"

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
    USERNAME_MAX_LENGTH: int = 32
    USERNAME_SPECIAL_CHARS: str = "_."
    USERNAME_REGEX: str = r"^[a-zA-Z0-9_\.]{4,32}$"

    @property
    def last_restart(self) -> datetime:
        return datetime.now(tz=ZoneInfo("UTC"))

    @property
    def project_desc(self) -> str:
        return (
            f"**Game Version: *`{self.in_game_version}`***\r\t\n"
            f"**Last restart: *`{self.last_restart.strftime('%Y-%m-%d %H:%M:%S %:z')}`***"  # noqa: E501
        )

    @property
    def in_game_version(self) -> str:
        return "4.7"


config = _BaseSettings()  # type: ignore
