
from pydantic import BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers, replace_icon
# from api.infra.entitys.relics.extra import Advancement
from api.infra.entitys.base import EntityBase


class Relic(EntityBase):
    name: str
    rarity: str
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    type: str
    icon: Annotated[str, BeforeValidator(replace_icon)]
    attributeID: str = Field(alias='AttributeID', serialization_alias='attributeID', exclude=True)
    advancement: list[str]

