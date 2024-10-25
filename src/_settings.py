from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ("config",)


class _BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None, case_sensitive=False)

    ENV: Literal["prod", "dev", "test"] = "dev"

    PROJECT_NAME: str = "Tower of Fantasy API"


config = _BaseSettings()
