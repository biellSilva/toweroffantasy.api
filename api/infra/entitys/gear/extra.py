from pydantic import AliasChoices, BaseModel, Field


class StatPool(BaseModel):
    propName: str = Field(validation_alias=AliasChoices("PropName"))
    weitghtValue: int | float = Field(validation_alias=AliasChoices("WeightValue"))


class BaseStat(BaseModel):
    isTag: bool = Field(validation_alias=AliasChoices("IsTag"))
    propName: str = Field(validation_alias=AliasChoices("PropName"))
    propValue: int | float = Field(validation_alias=AliasChoices("PropValue"))
    modifierOp: str = Field(validation_alias=AliasChoices("ModifierOp"))
