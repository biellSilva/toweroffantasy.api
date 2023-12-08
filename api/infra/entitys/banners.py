
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