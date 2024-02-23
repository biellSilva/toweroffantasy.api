from typing import Any, TypedDict


class RawMatrix(TypedDict):
    id: str
    name: str
    description: str
    rarity: int
    set: list[dict[str, str]]
    version: str
    weaponId: str | None
    sets: Any
    simulacrumId: str
    meta: dict[str, Any]
