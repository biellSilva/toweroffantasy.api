from datetime import datetime

from pytz import timezone


def to_lowercase(text: str) -> str:
    return text.lower().strip()


def to_strip(text: str) -> str:
    return text.strip()


def current_time() -> datetime:
    return datetime.now(timezone("UTC"))
