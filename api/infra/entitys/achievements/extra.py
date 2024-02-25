from pydantic import AliasChoices, BaseModel, Field


class Material(BaseModel):
    id: str
    name: str
    description: str
    icon: str
    rarity: int | None = None
    type: str | None = None


class Award(BaseModel):
    material: Material
    amount: int = Field(validation_alias=AliasChoices("amt"))
