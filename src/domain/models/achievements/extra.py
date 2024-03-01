from pydantic import AliasChoices, BaseModel, Field
import strawberry


class Reward(BaseModel):
    matId: str
    name: str
    description: str
    icon: str
    rarity: int | None = None
    type: str | None = None
    amount: int = Field(validation_alias=AliasChoices("amt"))


@strawberry.experimental.pydantic.type(model=Reward, all_fields=True)
class RewardType:
    pass
