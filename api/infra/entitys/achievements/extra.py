from pydantic import AliasChoices, BaseModel, Field


class Award(BaseModel):
    matId: str
    name: str
    description: str
    icon: str
    rarity: int | None = None
    type: str | None = None
    amount: int = Field(validation_alias=AliasChoices("amt"))
