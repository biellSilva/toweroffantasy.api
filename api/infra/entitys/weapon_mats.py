
from pydantic import BaseModel, Field, AliasChoices


class WeaponMat(BaseModel):
    id: str | None = Field(validation_alias=AliasChoices('mat_id', 'id'))
    amount: int | None = Field(validation_alias=AliasChoices('mat_amount', 'amount'))


class WeaponMats(BaseModel):
    id: str
    items: list[list[WeaponMat]]