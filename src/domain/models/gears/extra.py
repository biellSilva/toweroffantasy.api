import strawberry
from pydantic import AliasChoices, BaseModel, Field


class StatPool(BaseModel):
    propName: str = Field(validation_alias=AliasChoices("PropName"))
    weightValue: float = Field(validation_alias=AliasChoices("WeightValue"))
    name: str
    icon: str
    multiplier: float
    flat: bool


class BaseStat(BaseModel):
    isTag: bool = Field(validation_alias=AliasChoices("IsTag"))
    propName: str = Field(validation_alias=AliasChoices("PropName"))
    propValue: float = Field(validation_alias=AliasChoices("PropValue"))
    modifierOp: str = Field(validation_alias=AliasChoices("ModifierOp"))
    name: str
    icon: str
    multiplier: float
    flat: bool


class Prop(BaseModel):
    PropId: str
    Quality: str
    PropInitValue: float
    PropMinValue: float
    PropMaxValue: float


class GearAdvancement(BaseModel):
    matId: str = Field(validation_alias=AliasChoices("id"))
    name: str
    description: str
    rarity: int
    icon: str
    type: str
    amount: int = Field(validation_alias=AliasChoices("mat_amount", "matAmount"))


@strawberry.experimental.pydantic.type(model=StatPool, all_fields=True)
class StatPoolType:
    pass


@strawberry.experimental.pydantic.type(model=BaseStat, all_fields=True)
class BaseStatType:
    pass


@strawberry.experimental.pydantic.type(model=Prop, all_fields=True)
class PropType:
    pass


@strawberry.experimental.pydantic.type(model=GearAdvancement, all_fields=True)
class GearAdvancementType:
    pass
