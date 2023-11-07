
from pydantic import Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.simulacra.extra import VoiceActors


class Simulacra(EntityBase):
    name: str
    avatarID: str
    advanceID: str | None = Field(alias='advanceId', default=None)
    weapon: str
    icon: str
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str] = Field(alias='gp')
    voice_actors: VoiceActors = Field(alias='va')

