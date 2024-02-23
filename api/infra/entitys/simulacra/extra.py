from pydantic import BaseModel, BeforeValidator, Field, AliasChoices
from typing import Annotated

from api.utils import voice_actor_string_rework


class Assets(BaseModel):
    avatar: Annotated[
        str | None,
        BeforeValidator(
            lambda x: (
                str(x).rsplit(".", 1)[0]
                if isinstance(x, str) and ".webp.webp" in x
                else x
            )
        ),
    ] = ""
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
    # lotteryDrawing: str | None
    matrixPainting: str | None
    descPainting: str | None


class VoiceActors(BaseModel):
    cn: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    jp: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    en: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    kr: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    pt: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None


class Awakening(BaseModel):
    name: Annotated[str | None, BeforeValidator(lambda x: str(x).strip())] = None
    type: Annotated[str | None, BeforeValidator(lambda x: str(x).strip())] = None
    description: str | None = Field(
        None, validation_alias=AliasChoices("trait", "description")
    )
    icon: str | None = None
    need: int | None = Field(None, validation_alias=AliasChoices("stage", "need"))


class FashionAssets(BaseModel):
    painting: str
    grayPainting: str = Field(
        validation_alias=AliasChoices("prayPainting", "grayPainting")
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
