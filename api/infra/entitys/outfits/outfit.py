
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import replace_icon

from api.infra.entitys.base import EntityBase


class Outfit(EntityBase):
    name: str | None = None
    type: str
    description: str | None = None
    source: str | None = None
    icon: Annotated[str, BeforeValidator(replace_icon)]


