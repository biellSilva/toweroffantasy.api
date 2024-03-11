from typing import TYPE_CHECKING, TypedDict

from src.infra.models.simulacra.extra import (
    RawAwakening,
    RawFashion,
    RawNitai,
    RawSimulacraAssets,
    RawVoiceActors,
)

if TYPE_CHECKING:
    from src.domain.models.banner import Banner
    from src.domain.models.matrices import Matrix
    from src.domain.models.weapons import Weapon


class RawSimulacra(TypedDict):
    id: str
    name: str
    rarity: int
    version: str
    weaponId: str
    matrixId: str
    assetsA0: RawSimulacraAssets
    assetsA3: RawSimulacraAssets
    avatarId: str
    age: str | None
    height: str | None
    gender: str | None
    state: str | None
    city: str | None
    like: list[str]
    dislike: list[str]
    unlockInfo: str | None
    va: RawVoiceActors
    awakening: list[RawAwakening]
    fashion: list[RawFashion]
    nitai: list[RawNitai] | None
    weapon: "Weapon | None"
    matrix: "Matrix | None"
    banners: "list[Banner] | None"
