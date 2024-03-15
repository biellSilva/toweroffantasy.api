import strawberry
from pydantic import AliasChoices, BaseModel, Field


class GiftTag(BaseModel):
    tagId: str = Field(validation_alias=AliasChoices("giftId", "tagId"))
    name: str


@strawberry.experimental.pydantic.type(model=GiftTag, all_fields=True)
class GiftTagType:
    pass
