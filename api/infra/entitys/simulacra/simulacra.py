
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase

from .extra import VoiceActors as VC, Awakening, Assets
from ..banners import Banner


class Simulacra(EntityBase):
    name: str
    rarity: str
    # characterSex: str
    avatarId: str 
    advanceId: str | None = None
    # UnlockInfo: str
    weaponId: Annotated[str | None, BeforeValidator(lambda x: None 
                                                    if isinstance(x, str) and 
                                                    x.lower() == 'none' or 
                                                    x.lower() == 'null' else 
                                                    x)] = None 
    matrixId: Annotated[str | None, BeforeValidator(lambda x: None 
                                                    if isinstance(x, str) and 
                                                    x.lower() == 'none' or 
                                                    x.lower() == 'null' else 
                                                    x)] = None
    likedGiftTypes: list[str] = Field(alias='like')
    # dislikedGiftTypes: list[str] = Field(alias='dislike')
    gender: str | None = None
    birthday: str | None = Field(default=None, alias='age')
    # Age: str | None = None
    # Title: str | None = None
    # Job: str | None = None
    height: str | None = None
    affiliation: str | None = Field(default=None, alias='state')
    homeTown: str | None = Field(default=None, alias='city')
    assetsA0: Assets
    assetsA3: Assets | None = None
    voicing: VC = Field(alias='va')
    awakening: list[Awakening]
    banners: list[Banner]
