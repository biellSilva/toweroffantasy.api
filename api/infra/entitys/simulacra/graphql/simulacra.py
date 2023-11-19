
import strawberry

from api.infra.entitys.banners import BannerSchema
from .extra import Assets, VoiceActors, Awakening


@strawberry.type()
class Simulacra:
    id: str
    name: str
    rarity: str | None
    avatarID: str
    advanceID: str | None
    assets: Assets
    weaponID: str | None
    matrixID: str | None
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str] 
    voice_actors: VoiceActors
    awakenings: list[Awakening]
    banners: list[BannerSchema]
