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


@strawberry.experimental.pydantic.type(model=StatPool, all_fields=True)
class StatPoolType:
    pass


@strawberry.experimental.pydantic.type(model=BaseStat, all_fields=True)
class BaseStatType:
    pass


@strawberry.experimental.pydantic.type(model=Prop, all_fields=True)
class PropType:
    pass
