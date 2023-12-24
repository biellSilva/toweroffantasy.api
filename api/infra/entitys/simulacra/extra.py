
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import voice_actor_string_rework, replace_icon


class Assets(BaseModel):
    avatar: Annotated[str | None, BeforeValidator(replace_icon)] 
    titlePicture: Annotated[str | None, BeforeValidator(replace_icon)] 
    characterArtwork: Annotated[str | None, BeforeValidator(replace_icon)] 
    painting: Annotated[str | None, BeforeValidator(replace_icon)] 
    namePicture: Annotated[str | None, BeforeValidator(replace_icon)] 
    grayPainting: Annotated[str | None, BeforeValidator(replace_icon)] 
    thumbPainting: Annotated[str | None, BeforeValidator(replace_icon)] 
    weaponShowPicture: Annotated[str | None, BeforeValidator(replace_icon)] 
    activeImitation: Annotated[str | None, BeforeValidator(replace_icon)] 
    inactiveImitation:Annotated[str | None, BeforeValidator(replace_icon)] 
    advancePainting: Annotated[str | None, BeforeValidator(replace_icon)] 
    advanceGrayPainting: Annotated[str | None, BeforeValidator(replace_icon)] 
    backPhoto: Annotated[str | None, BeforeValidator(replace_icon)] 
    rarityIcon: Annotated[str | None, BeforeValidator(replace_icon)] 
    lotteryCardImage: Annotated[str | None, BeforeValidator(replace_icon)] 
    # lotteryDrawing: Annotated[str | None, BeforeValidator(replace_icon)] 
    matrixPainting: Annotated[str | None, BeforeValidator(replace_icon)] 
    descPainting: str


class VoiceActors(BaseModel):
    cn: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    jp: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    en: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    kr: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    pt: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None


class Awakening(BaseModel):
    name: str
    description: str
    icon: Annotated[str | None, BeforeValidator(replace_icon)] 
    need: int
