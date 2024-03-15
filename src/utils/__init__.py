import re
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


def string_or_null(text: str) -> str | None:
    if text.lower() in ("none", "null"):
        return None
    return text.lower()


def bold_numbers(text: str) -> str:
    text_a = re.sub(
        r"\<[a-zA-Z]+\>(\D)+\<\/\>",
        lambda x: (
            x.group(0)
            .replace("<shuzhi>", "**")
            .replace("<red>", "**")
            .replace("<blue>", "**")
            .replace("<green>", "**")
            .replace("<ComLblGreen>", "**")
            .replace("</>", "**")
            if text[x.span(0)[0] - 1] != "*"
            else x.group(0)
        ),
        text,
        flags=re.UNICODE,
    )

    text_b = re.sub(
        r"\+?\{?\d+(\.?\,?\d+)?\}?%?",
        lambda x: (
            f"**{x.group(0)}**" if text_a[x.span(0)[0] - 1] != "*" else x.group(0)
        ),
        text_a.replace("<shuzhi>", "")
        .replace("<red>", "")
        .replace("<blue>", "")
        .replace("<green>", "")
        .replace("</>", ""),
        flags=re.UNICODE,
    )

    return text_b


def banner_datetime_to_iso(date: datetime) -> str:
    return date.isoformat()
