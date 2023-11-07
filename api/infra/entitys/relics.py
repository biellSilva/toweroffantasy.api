
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import bold_numbers


class RelicAdvancement(BaseModel):
    id: str
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    
class Relic(BaseModel):
    id: str
    name: str
    rarity: str
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    type: str
    icon: str
    advancement: list[RelicAdvancement]

