

from api.infra.entitys.base import EntityBase
from api.infra.entitys.weapons import Weapon
from api.infra.entitys.matrices import Matrix
from api.infra.entitys.simulacra.extra import Awakening, VoiceActors, Banner

from .extra import Assets



class Simulacra_v2(EntityBase):
    name: str
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

