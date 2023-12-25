
from pydantic import BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers, relic_advanc_rework

from api.infra.entitys.base import EntityBase


class Relic(EntityBase):
    name: str
    rarity: str
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    type: str
    icon: str | None
    # attributeID: str = Field(alias='AttributeID', serialization_alias='attributeID', exclude=True)
    advancements: Annotated[list[str], BeforeValidator(relic_advanc_rework)] = Field(alias='advancement', serialization_alias='advancements')

