
import strawberry

from api.infra.entitys.graphql.banner import Banner
from .extra import Assets, VoiceActors as VC, Awakening


@strawberry.type()
class Simulacra:
    id: str
    name: str
    version: str
    isReleased: bool
    rarity: int
    # sex: str
    avatarId: str 
    advanceId: str | None 
    # UnlockInfo: str
    weaponId: str | None 
    matrixId: str | None 
    likedGiftTypes: list[str] 
    # dislikedGiftTypes: list[str] = Field(alias='dislike')
    gender: str | None 
    birthday: str | None
    # Age: str | None = None
    # Title: str | None = None
    # Job: str | None = None
    height: str | None 
    affiliation: str | None
    homeTown: str | None
    assetsA0: Assets
    assetsA3: Assets | None
    voicing: VC 
    awakening: list[Awakening]
    banners: list[Banner]
