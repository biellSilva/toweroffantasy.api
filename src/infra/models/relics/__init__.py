from typing import TypedDict


class RawRelic(TypedDict):
    id: str
    version: str
    advancement: list[dict[str, str]]
    advancements: list[str]
