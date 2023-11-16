
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import replace_cv, replace_icon, put_imitation_icon


class VoiceActors(BaseModel):
    chinese: Annotated[str, BeforeValidator(replace_cv)] | None = None
    japanese: Annotated[str, BeforeValidator(replace_cv)] | None = None
    english: Annotated[str, BeforeValidator(replace_cv)] | None = None
    korean: Annotated[str, BeforeValidator(replace_cv)] | None = None
    portuguese: Annotated[str, BeforeValidator(replace_cv)] | None = None


class Awakening(BaseModel):
    name: str
    description: str


class Assets(BaseModel):
    avatar: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    artwork: Annotated[str, BeforeValidator(put_imitation_icon)] | None = Field(default=None, alias='icon', serialization_alias='artwork')
    lotteryCard: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='LotteryCardImage', serialization_alias='lotteryCard')
    lotteryDrawing: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='LotteryDrawing', serialization_alias='lotteryDrawing')


class Banner(BaseModel):
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool
