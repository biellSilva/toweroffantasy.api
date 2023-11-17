
from pydantic import BaseModel, Field, BeforeValidator
from typing import Annotated

from api.utils import replace_icon


class ServantAsset(BaseModel):
    petIcon: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='PetIcon', serialization_alias='petIcon')
    activatedIcon: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='PetActivatedIcon', serialization_alias='activatedIcon')
    itemIcon: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='ItemIcon', serialization_alias='itemIcon')


class ServantSkill(BaseModel):
    name: str
    description: str
    icon: Annotated[str, BeforeValidator(replace_icon)]


class ServantUpgrade(BaseModel):
    id: str
    xpGain: int