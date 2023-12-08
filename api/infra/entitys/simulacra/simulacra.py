
from pydantic import Field

from api.infra.entitys.base import EntityBase

from .extra import VoiceActors as VC, Awakening, Assets
from ..banners import Banner


class Simulacra(EntityBase):
    name: str
    rarity: str
    # sex: str
    avatarId: str 
    advanceId: str | None = None
    # UnlockInfo: str
    weaponId: str | None = None
    matrixId: str | None = None
    likedGiftTypes: list[str] = Field(alias='like')
    # dislikedGiftTypes: list[str] = Field(alias='dislike')
    gender: str | None = None
    birthday: str | None = Field(alias='age')
    # Age: str | None = None
    # Title: str | None = None
    # Job: str | None = None
    height: str | None = None
    affiliation: str | None = Field(default=None, alias='state', serialization_alias='affiliation')
    hometown: str | None = Field(default=None, serialization_alias='city')
    assetsA0: Assets
    assetsA3: Assets | None = None
    voicing: VC
    awakening: list[Awakening]
    banners: list[Banner]
