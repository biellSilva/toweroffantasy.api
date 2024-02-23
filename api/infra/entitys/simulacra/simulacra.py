from typing import Annotated

from pydantic import AliasChoices, BeforeValidator, Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.guidebooks.extra import GuideBookItem

from ..banners import Banner
from .extra import Assets, Awakening, Fashion
from .extra import VoiceActors as VC


class Simulacra(EntityBase):
    name: str
    rarity: int
    version: str
    isReleased: bool = True
    avatarId: str
    advanceId: str | None = None
    unlockInfo: str
    limited: bool

    weaponId: Annotated[
        str | None,
        BeforeValidator(
            lambda x: (
                None
                if not x
                or (isinstance(x, str) and (x.lower() == "none" or x.lower() == "null"))
                else x.lower()
            )
        ),
    ] = None
    matrixId: Annotated[
        str | None,
        BeforeValidator(
            lambda x: (
                None
                if not x
                or (isinstance(x, str) and (x.lower() == "none" or x.lower() == "null"))
                else x.lower()
            )
        ),
    ] = None

    likedGiftTypes: list[str] = Field(
        default=[], validation_alias=AliasChoices("like", "likedGiftTypes")
    )
    dislikedGiftTypes: list[str] = Field(
        default=[], validation_alias=AliasChoices("dislike", "dislikedGiftTypes")
    )
    gender: str | None = None
    birthday: str | None = Field(
        default=None, validation_alias=AliasChoices("age", "birthday")
    )
    height: str | None = None
    affiliation: str | None = Field(
        default=None, validation_alias=AliasChoices("state", "affiliation")
    )
    homeTown: str | None = Field(
        default=None, validation_alias=AliasChoices("city", "homeTown")
    )
    assetsA0: Assets
    assetsA3: Assets | None = None
    voicing: VC = Field(validation_alias=AliasChoices("va", "voicing"))
    awakening: list[Awakening]
    banners: list[Banner] = []
    fashion: list[Fashion] = []
    guidebook: Annotated[
        list[GuideBookItem],
        Field(default=[], validation_alias=AliasChoices("nitai", "guidebook")),
    ]
