
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.utils import replace_icon

from api.infra.entitys.base import EntityBase
from api.infra.entitys.simulacra.extra import VoiceActors, Awakening
from api.infra.entitys.weapons import Weapon
from api.infra.entitys.matrices import Matrice


class Simulacra_v2(EntityBase):
    name: str
    icon: Annotated[str, BeforeValidator(replace_icon)]
    avatarID: str
    advanceId: str | None = None
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str]
    voice_actors: VoiceActors
    awakenings: list[Awakening] = Field(alias='trait', default=[], serialization_alias='awakenings')
    weapon: Weapon | None = None
    matrice: Matrice | None = None

