
from pydantic import BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from api.utils import replace_icon


class Item(EntityBase):
    id: str
    name: str | None = None
    type: str
    description: str | None = None
    icon: Annotated[str, BeforeValidator(replace_icon)]
    rarity: str
    