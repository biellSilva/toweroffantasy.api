
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import replace_cv, replace_icon


class VoiceActors(BaseModel):
    chinese: Annotated[str | None, BeforeValidator(replace_cv)]  = None
    japanese: Annotated[str | None, BeforeValidator(replace_cv)] = None
    english: Annotated[str | None, BeforeValidator(replace_cv)] = None
    korean: Annotated[str | None, BeforeValidator(replace_cv)] = None
    portuguese: Annotated[str | None, BeforeValidator(replace_cv)] = None


class Awakening(BaseModel):
    name: str
    description: str


class Assets(BaseModel):
    avatar: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    artwork: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='icon', serialization_alias='artwork')
    lotteryCard: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='LotteryCardImage', serialization_alias='lotteryCard')
    lotteryDrawing: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='LotteryDrawing', serialization_alias='lotteryDrawing')
    painting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='Painting', serialization_alias='painting')
    grayPainting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='GrayPainting', serialization_alias='grayPainting')
    namePicture: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='NamePicture', serialization_alias='namePicture')
    thumbPainting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='ThumbPainting', serialization_alias='thumbPainting')
    weaponPicture: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='WeaponShowPicture', serialization_alias='weaponPicture')
    awakenEntrance: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='HasGotAwakenEntrance', serialization_alias='awakenEntrance')
    grayAwakenEntrance: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='NotGotAwakenEntrance', serialization_alias='grayAwakenEntrance')
    advancePainting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='AdvancePainting', serialization_alias='advancePainting')
    grayAdvancePainting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='AdvanceGrayPainting', serialization_alias='grayAdvancePainting')
    backPhoto: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='BackPhoto', serialization_alias='backPhoto')
    rarityIcon: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='RarityIcon', serialization_alias='rarityIcon')
    bannerIcon: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='SoloLeagueBanPickBanner', serialization_alias='bannerIcon')



