
from pydantic import BaseModel, Field, AliasChoices, BeforeValidator
from typing import Annotated


class WeaponMat(BaseModel):
    id: Annotated[str | None, BeforeValidator(lambda x: x if x and str(x).lower() != 'none' else None)] = Field(validation_alias=AliasChoices('mat_id', 'id'))
    amount: int | None = Field(validation_alias=AliasChoices('mat_amount', 'amount'))
    name: str | None = None
    icon: str | None = None
    type: str | None = None
    description: str | None = None
    rarity: str | None = None


class WeaponMats(BaseModel):
    id: str
    items: list[list[WeaponMat]]