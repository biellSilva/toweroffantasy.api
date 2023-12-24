
from pydantic import Field, BeforeValidator, AliasChoices
from typing import Annotated

from api.infra.entitys.base import EntityBase

from .extra import VoiceActors as VC, Awakening, Assets
from ..banners import Banner


class Simulacra(EntityBase):
    name: str
    rarity: str
    version: str
    # characterSex: str
    avatarId: str 
    advanceId: str | None = None
    # UnlockInfo: str
    
    weaponId: Annotated[str | None, BeforeValidator(lambda x: None if not x or (isinstance(x, str) and (x.lower() == 'none' or x.lower() == 'null')) else x)] = None 
    matrixId: Annotated[str | None, BeforeValidator(lambda x: None if not x or (isinstance(x, str) and (x.lower() == 'none' or x.lower() == 'null')) else x)] = None

    likedGiftTypes: list[str] = Field(validation_alias=AliasChoices('like', 'likedGiftTypes'))
    # dislikedGiftTypes: list[str] = Field(validation_alias='dislike')
    gender: str | None = None
    birthday: str | None = Field(default=None, validation_alias=AliasChoices('age', 'birthday'))
    # Age: str | None = None
    # Title: str | None = None
    # Job: str | None = None
    height: str | None = None
    affiliation: str | None = Field(default=None, validation_alias=AliasChoices('state', 'affiliation'))
    homeTown: str | None = Field(default=None, validation_alias=AliasChoices('city', 'homeTown'))
    assetsA0: Assets
    assetsA3: Assets | None = None
    voicing: VC = Field(validation_alias=AliasChoices('va', 'voicing'))
    awakening: list[Awakening]
    banners: list[Banner]
