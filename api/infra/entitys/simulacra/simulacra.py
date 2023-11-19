
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from .extra import VoiceActors, Awakening, Assets, Banner

from api.utils import check_string, voice_actors_rework, replace_icon, trait_rework


class Simulacra(EntityBase):
    name: str = 'MISSING'
    rarity: str | None
    avatarID: str
    advanceID: str | None = Field(default=None, alias='advanceId', serialization_alias='advanceID')
    assets: Assets
    weaponID: Annotated[str | None, BeforeValidator(check_string)] = Field(default=None, alias='weapon', serialization_alias='weaponID')
    matrixID: str | None = None
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: Annotated[str, BeforeValidator(replace_icon)]
    gift_types: list[str] = Field(alias='gp', serialization_alias='gift_types')
    voice_actors: Annotated[VoiceActors, BeforeValidator(voice_actors_rework)] = Field(alias='va', serialization_alias='voice_actors')
    awakenings: Annotated[list[Awakening], BeforeValidator(trait_rework)] = Field(alias='trait', default=[], serialization_alias='awakenings')
    banners: list[Banner] = []

