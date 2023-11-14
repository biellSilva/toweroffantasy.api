
import strawberry

from .extra import Assets, VoiceActors, Awakening


@strawberry.type()
class SimulacraType:
    id: str
    name: str
    avatarID: str
    advanceId: str | None
    assets: Assets
    weapon_id: str
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str] 
    voice_actors: VoiceActors
    awakenings: list[Awakening]

