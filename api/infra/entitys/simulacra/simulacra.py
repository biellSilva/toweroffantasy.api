
from pydantic import Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.simulacra.extra import VoiceActors, Awakening


class Simulacra(EntityBase):
    name: str
    avatarID: str = Field(alias='avatarID', serialization_alias='avatar_id')
    advance_id: str | None = Field(alias='advanceId', default=None, serialization_alias='advance_id')
    weapon: str
    icon: str
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str] = Field(alias='gp', serialization_alias='gift_types')
    voice_actors: VoiceActors = Field(alias='va', serialization_alias='voice_actors')
    awakenings: list[Awakening] = Field(alias='trait', default=[], serialization_alias='awakenings')

