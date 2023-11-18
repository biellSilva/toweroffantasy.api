
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import put_imitation_icon, replace_icon


class Assets(BaseModel):
    avatar: Annotated[str, BeforeValidator(replace_icon)] | None 
    artwork: Annotated[str, BeforeValidator(put_imitation_icon)] | None
    lotteryCard: Annotated[str, BeforeValidator(replace_icon)] | None
    lotteryDrawing: Annotated[str, BeforeValidator(replace_icon)] | None
    painting: Annotated[str, BeforeValidator(replace_icon)] | None
    grayPainting: Annotated[str, BeforeValidator(replace_icon)] | None
    namePicture: Annotated[str, BeforeValidator(replace_icon)] | None
    thumbPainting: Annotated[str, BeforeValidator(replace_icon)] | None
    weaponPicture: Annotated[str, BeforeValidator(replace_icon)] | None
    awakenEntrance: Annotated[str, BeforeValidator(replace_icon)] | None
    grayAwakenEntrance: Annotated[str, BeforeValidator(replace_icon)] | None
    advancePainting: Annotated[str, BeforeValidator(replace_icon)] | None
    grayAdvancePainting: Annotated[str, BeforeValidator(replace_icon)] | None
    backPhoto: Annotated[str, BeforeValidator(replace_icon)] | None
    rarityIcon: Annotated[str, BeforeValidator(replace_icon)] | None
    bannerIcon: Annotated[str, BeforeValidator(replace_icon)] | None 
