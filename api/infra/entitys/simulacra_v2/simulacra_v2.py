

from api.infra.entitys.base import EntityBase
from api.infra.entitys.weapons import Weapon
from api.infra.entitys.matrices import Matrice
from api.infra.entitys.simulacra.extra import Awakening, VoiceActors, Banner

from .extra import Assets


class Simulacra_v2(EntityBase):
    name: str
    avatarID: str
    advanceId: str | None = None
    assets: Assets
    weapon_id: str | None
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
    matrice: Matrice | None = None

