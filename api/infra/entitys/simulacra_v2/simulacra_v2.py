
from pydantic import Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.simulacra_v2.extra import VoiceActors
from api.infra.entitys.weapons import Weapon
from api.infra.entitys.matrices import Matrice


class Simulacra_v2(EntityBase):
    name: str
    icon: str
    advanceID: str | None = Field(alias='advanceId', default=None)
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str]
    voice_actors: VoiceActors
    weapon: Weapon | None = None
    matrice: Matrice | None = None

