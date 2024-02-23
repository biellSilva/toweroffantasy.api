from typing import Annotated

from pydantic import AliasChoices, BaseModel, BeforeValidator, Field
from src.utils import to_strip

from src.utils.simulacra import voice_actor_rework


class VoiceActors(BaseModel):
    cn: Annotated[str, BeforeValidator(voice_actor_rework)] | None = None
    jp: Annotated[str, BeforeValidator(voice_actor_rework)] | None = None
    en: Annotated[str, BeforeValidator(voice_actor_rework)] | None = None
    kr: Annotated[str, BeforeValidator(voice_actor_rework)] | None = None
    pt: Annotated[str, BeforeValidator(voice_actor_rework)] | None = None


class SimulacraAssets(BaseModel):
    avatar: str | None
    titlePicture: str | None
    characterArtwork: str | None
    painting: str | None
    namePicture: str | None
    grayPainting: str | None
    thumbPainting: str | None
    weaponShowPicture: str | None
    activeImitation: str | None
    inactiveImitation: str | None
    advancePainting: str | None
    advanceGrayPainting: str | None
    backPhoto: str | None
    rarityIcon: str | None
    lotteryCardImage: str | None
    matrixPainting: str | None
    descPainting: str | None


class Awakening(BaseModel):
    name: Annotated[str, BeforeValidator(to_strip)] | None = None
    description: str | None = Field(
        None, validation_alias=AliasChoices("trait", "description")
    )
    icon: str | None = None
    need: int | None = Field(None, validation_alias=AliasChoices("stage", "need"))


class FashionAssets(BaseModel):
    painting: str
    grayPainting: str = Field(
        validation_alias=AliasChoices("grayPainting", "prayPainting")
    )


class Fashion(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    source: str
    simulacrumId: str
    weaponId: str
    assets: FashionAssets
