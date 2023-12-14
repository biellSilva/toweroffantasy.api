
from pydantic import BaseModel, BeforeValidator, Field, model_validator, AliasChoices
from typing import Annotated, Any
from pathlib import Path
from json import loads


weapons_data: dict[str, Any] = loads(Path('api/infra/database/global/en/weapons.json').read_bytes())


class Banner(BaseModel):
    simulacrumId: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, validation_alias=AliasChoices('imitation_id', 'simulacrumId'))
    weaponId: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, validation_alias=AliasChoices('weapon_id', 'weaponId'))
    matrixId: Annotated[str, BeforeValidator(lambda x: str(x).lower())] | None = Field(default=None, validation_alias=AliasChoices('matrix_id', 'matrixId'))
    simulacrumName: str | None = Field(default=None, validation_alias=AliasChoices('simulacrum', 'simulacrumName'))
    bannerNumber: int = Field(validation_alias=AliasChoices('bannerNo', 'bannerNumber'))
    element: str | None = None
    category: str | None = None
    startDate: str = Field(validation_alias=AliasChoices('start', 'startDate'))
    endDate: str = Field(validation_alias=AliasChoices('end', 'endDate'))
    detailsLink: str = Field(validation_alias=AliasChoices('details_link', 'detailsLink'))
    isLimitedBannerOnly: bool = Field(validation_alias=AliasChoices('limited_banner_only', 'isLimitedBannerOnly'))
    isRerun: bool = Field(validation_alias=AliasChoices('is_rerun', 'isRerun'))
    isFinalBanner: bool = Field(validation_alias=AliasChoices('final_rerun', 'isFinalBanner'))
    isCollab: bool = Field(validation_alias=AliasChoices('is_collab', 'isCollab'))
    noWeapon: bool = Field(validation_alias=AliasChoices('no_weapon', 'noWeapon'))

    @model_validator(mode='before')
    def add_element_and_category(cls, value: dict[str, Any]):
        if weapon_data := weapons_data.get(value.get('weapon_id', ''), None):
            value['element'] = weapon_data['element']
            value['category'] = weapon_data['wc']
        
        return value