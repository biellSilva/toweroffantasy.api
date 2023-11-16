
import strawberry

from .extra import Assets, VoiceActors, Awakening, Banner


@strawberry.type()
class SimulacraType:
    id: str
    name: str
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
    banners: list[Banner]
