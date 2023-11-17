
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from api.infra.entitys.simulacra.extra import VoiceActors, Awakening, Assets, Banner

from api.utils import check_string


class Simulacra(EntityBase):
    name: str
    rarity: str | None
    avatarID: str
    advanceID: str | None = Field(default=None, alias='advanceId', serialization_alias='advanceID')
    assets: Assets
    weaponID: Annotated[str | None, BeforeValidator(check_string)] = Field(default=None, alias='weapon', serialization_alias='weaponID')
    matrixID: str | None
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str] = Field(alias='gp', serialization_alias='gift_types')
    voice_actors: VoiceActors = Field(alias='va', serialization_alias='voice_actors')
    awakenings: list[Awakening] = Field(alias='trait', default=[], serialization_alias='awakenings')
    banners: list[Banner] = []

