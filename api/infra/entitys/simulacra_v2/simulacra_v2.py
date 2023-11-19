

from api.infra.entitys.base import EntityBase
from ..weapons import Weapon
from ..matrices import Matrix
from ..simulacra.extra import Awakening, VoiceActors, Banner

from .extra import Assets



class Simulacra_v2(EntityBase):
    name: str
    rarity: str | None
    avatarID: str
    advanceID: str | None = None
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
    weapon: Weapon | None = None
    matrix: Matrix | None = None

