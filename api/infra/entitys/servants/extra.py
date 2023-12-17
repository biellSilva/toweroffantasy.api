
from pydantic import BaseModel, Field, BeforeValidator
from typing import Annotated

from api.utils import replace_icon


class ServantAsset(BaseModel):
    petIcon: Annotated[str, BeforeValidator(replace_icon)] = Field(validation_alias='petIcon')
    activatedIcon: Annotated[str, BeforeValidator(replace_icon)] = Field(validation_alias='petActivatedIcon')
    itemIcon: Annotated[str, BeforeValidator(replace_icon)] = Field(validation_alias='itemIcon')


class ServantSkill(BaseModel):
    name: str
    description: str
    icon: Annotated[str, BeforeValidator(replace_icon)]


class ServantUpgrade(BaseModel):
    id: str
    xpGain: int