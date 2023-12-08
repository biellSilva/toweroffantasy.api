
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated


class Banner(BaseModel):
    simulacrumId: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, alias='imitation_id')
    weaponId: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, alias='weapon_id')
    matrixId: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, alias='matrix)_id')
    simulacrumName: str | None = Field(default=None, alias='simulacrum')
    bannerNumber: int = Field(alias='bannerNo')
    startDate: str = Field(alias='start')
    endDate: str = Field(alias='end')
    detailsLink: str = Field(alias='details_link')
    isLimitedBannerOnly: bool = Field(alias='limited_banner_only')
    isRerun: bool = Field(alias='is_rerun')
    isFinalBanner: bool = Field(alias='final_rerun')
    isCollab: bool = Field(alias='is_collab')