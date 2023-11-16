
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import put_imitation_icon, replace_icon


class Assets(BaseModel):
    avatar: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    artwork: Annotated[str, BeforeValidator(put_imitation_icon)] | None = None
    lotteryCard: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    lotteryDrawing: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    painting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    grayPainting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    namePicture: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    thumbPainting: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    weaponPicture: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    awakenEntrance: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
    grayAwakenEntrance: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None)
