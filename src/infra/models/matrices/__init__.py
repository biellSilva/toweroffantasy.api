from typing import TYPE_CHECKING, Any, TypedDict

if TYPE_CHECKING:
    from src.domain.models.banner import Banner


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
    banners: list["Banner"]
