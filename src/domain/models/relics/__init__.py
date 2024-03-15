from typing import Annotated

import strawberry
from pydantic import BeforeValidator

from src.domain.models.base import ModelBase
from src.utils import bold_numbers


class Relic(ModelBase):
    name: str
    rarity: int
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    type: str
    icon: str | None = None
    version: str | None = None
    advancements: list[str]


@strawberry.experimental.pydantic.type(model=Relic, all_fields=True)
class RelicType:
    pass
