from typing import Annotated

from pydantic import AliasChoices, BeforeValidator, Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.guidebooks.extra import GuideBookItem


class GuideBook(EntityBase):
    name: str
    icon: str
    items: Annotated[
        list[GuideBookItem],
        Field(default=[], validation_alias=AliasChoices("array", "items")),
    ]
    menuId: Annotated[str, BeforeValidator(lambda x: str(x).lower())]
    menuType: Annotated[str, BeforeValidator(lambda x: str(x).lower())]
