from typing import Annotated

from pydantic import AliasChoices, BaseModel, BeforeValidator, Field

from src.utils import to_lowercase


class Banner(BaseModel):
    simulacrumId: Annotated[str, BeforeValidator(to_lowercase)] | None = Field(
        default=None, validation_alias=AliasChoices("imitation_id", "simulacrumId")
    )
    weaponId: Annotated[str, BeforeValidator(to_lowercase)] | None = Field(
        default=None, validation_alias=AliasChoices("weapon_id", "weaponId")
    )
    matrixId: Annotated[str, BeforeValidator(to_lowercase)] | None = Field(
        default=None, validation_alias=AliasChoices("matrix_id", "matrixId")
    )
    simulacrumName: str | None = Field(
        default=None, validation_alias=AliasChoices("simulacrum", "simulacrumName")
    )
    bannerNumber: int = Field(validation_alias=AliasChoices("bannerNo", "bannerNumber"))
    element: str | None = None
    category: str | None = None
    startDate: str = Field(validation_alias=AliasChoices("start", "startDate"))
    endDate: str = Field(validation_alias=AliasChoices("end", "endDate"))
    detailsLink: str = Field(
        validation_alias=AliasChoices("details_link", "detailsLink")
    )
    isLimitedBannerOnly: bool = Field(
        validation_alias=AliasChoices("limited_banner_only", "isLimitedBannerOnly")
    )
    isRerun: bool = Field(validation_alias=AliasChoices("is_rerun", "isRerun"))
    isFinalBanner: bool = Field(
        validation_alias=AliasChoices("final_rerun", "isFinalBanner")
    )
    isCollab: bool = Field(validation_alias=AliasChoices("is_collab", "isCollab"))
    isReleased: bool = True
