import strawberry

from api.infra.entitys.graphql.banner import Banner
from api.infra.entitys.guidebooks.graphql import GuideBookItem
from .extra import Assets, VoiceActors as VC, Awakening, Fashion


@strawberry.type()
class Simulacra:
    id: str
    name: str
    version: str
    isReleased: bool
    rarity: int
    avatarId: str
    advanceId: str | None
    unlockInfo: str
    weaponId: str | None
    matrixId: str | None
    likedGiftTypes: list[str]
    dislikedGiftTypes: list[str]
    gender: str | None
    birthday: str | None
    height: str | None
    affiliation: str | None
    homeTown: str | None
    assetsA0: Assets
    assetsA3: Assets | None
    voicing: VC
    awakening: list[Awakening]
    banners: list[Banner]
    fashion: list[Fashion]
    guidebook: list[GuideBookItem]
