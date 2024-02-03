from pydantic import BaseModel, Field, AliasChoices, BeforeValidator
from typing import Annotated


class UpgradeMaterial(BaseModel):
    matId: Annotated[
        str | None,
        BeforeValidator(lambda x: x if x and str(x).lower() != "none" else None),
    ] = Field(validation_alias=AliasChoices("mat_id", "matId"))
    amount: int | None = Field(validation_alias=AliasChoices("mat_amount", "amount"))
    name: str | None = None
    icon: str | None = None
    type: str | None = None
    description: str | None = None
    rarity: int | None = None


class LevelUpgrade(BaseModel):
    requiredExp: int
    mats: list[UpgradeMaterial]


class WeaponMats(BaseModel):
    id: str
    levels: list[LevelUpgrade]
