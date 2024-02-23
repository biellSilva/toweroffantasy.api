from typing import TypedDict

from src.infra.models.simulacra.extra import (
    RawAwakening,
    RawFashion,
    RawNitai,
    RawSimulacraAssets,
    RawVoiceActors,
)


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
