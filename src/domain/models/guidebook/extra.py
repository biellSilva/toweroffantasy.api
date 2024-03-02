from typing import Annotated

import strawberry
from pydantic import AliasChoices, BaseModel, Field


class GuideBookItem(BaseModel):
    title: str
    description: str
    icon: Annotated[str, Field(validation_alias=AliasChoices("icon", "photo"))]


@strawberry.experimental.pydantic.type(model=GuideBookItem, all_fields=True)
class GuideBookItemType:
    pass
