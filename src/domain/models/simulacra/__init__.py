from typing import Annotated

from pydantic import AliasChoices, BeforeValidator, Field

from src.domain.models.banner import Banner
from src.domain.models.base import ModelBase
from src.domain.models.guidebook.extra import GuideBookItem
from src.domain.models.simulacra.extra import (
    Awakening,
    Fashion,
    SimulacraAssets,
    VoiceActors,
)
from src.utils.simulacra import weapon_matrix_rework


class Simulacra(ModelBase):
    name: str
    rarity: int
    isReleased: bool = True
    avatarId: str
    advanceId: str | None = None
    unlockInfo: str
    weaponId: Annotated[str, BeforeValidator(weapon_matrix_rework)] | None = None
    matrixId: Annotated[str, BeforeValidator(weapon_matrix_rework)] | None = None
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
    assetsA0: SimulacraAssets
    assetsA3: SimulacraAssets | None = None
    voicing: VoiceActors = Field(validation_alias=AliasChoices("va", "voicing"))
    awakening: list[Awakening]
    banners: list[Banner] = []
    fashion: list[Fashion] = []
    guidebook: list[GuideBookItem] = Field(
        default=[], validation_alias=AliasChoices("nitai", "guidebook")
    )