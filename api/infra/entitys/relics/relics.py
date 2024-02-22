from pydantic import BeforeValidator, Field, AliasChoices
from typing import Annotated

from api.utils import bold_numbers, relic_advanc_rework

from api.infra.entitys.base import EntityBase


class Relic(EntityBase):
    name: str
    rarity: int
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    type: str
    icon: str | None
    version: str
    # attributeID: str = Field(alias='AttributeID', serialization_alias='attributeID', exclude=True)
    advancements: Annotated[list[str], BeforeValidator(relic_advanc_rework)] = Field(
        validation_alias=AliasChoices("advancements", "advancement")
    )
