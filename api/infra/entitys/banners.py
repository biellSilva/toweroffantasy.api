
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated


class Banner(BaseModel):
    imitation_id: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, serialization_alias='simulacrumId')
    weapon_id: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, serialization_alias='weaponId')
    matrix_id: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, serialization_alias='matrixId')
    simulacrum: str | None = Field(default=None, serialization_alias='simulacrumName')
    bannerNo: int = Field(serialization_alias='BannerNumber')
    start: str = Field(serialization_alias='startDate')
    end: str = Field(serialization_alias='endDate')
    details_link: str = Field(serialization_alias='detailsLink')
    limited_banner_only: bool = Field(serialization_alias='isLimitedBannerOnly')
    is_rerun: bool = Field(serialization_alias='isRerun')
    final_rerun: bool = Field(serialization_alias='isFinalBanner')
    is_collab: bool = Field(serialization_alias='isCollab')

