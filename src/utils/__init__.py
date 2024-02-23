import tomllib
from datetime import datetime

from pytz import timezone

from . import __models


def to_lowercase(text: str) -> str:
    return text.lower().strip()


def to_strip(text: str) -> str:
    return text.strip()


def current_time() -> datetime:
    return datetime.now(timezone("UTC"))


def project_toml() -> __models.Project:
    with open("./pyproject.toml", "rb") as f:
        return __models.PyProject(**tomllib.load(f)).project
