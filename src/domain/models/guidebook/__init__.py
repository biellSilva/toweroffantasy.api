from typing import Annotated

import strawberry
from pydantic import AliasChoices, BeforeValidator, Field

from src.domain.models.base import ModelBase
from src.domain.models.guidebook.extra import GuideBookItem
from src.utils import to_lowercase


class GuideBook(ModelBase):
    name: str
    icon: str
    items: list[GuideBookItem] = Field(
        default=[], validation_alias=AliasChoices("array", "items")
    )
    menuId: Annotated[str, BeforeValidator(to_lowercase)]
    menuType: Annotated[str, BeforeValidator(to_lowercase)]


@strawberry.experimental.pydantic.type(model=GuideBook, all_fields=True)
class GuideBookType:
    pass
