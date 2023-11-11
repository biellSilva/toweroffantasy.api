
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import replace_icon
from api.infra.entitys.base import EntityBase
from .extra import Award


class Achievement(EntityBase):
    name: str
    description: str
    icon: Annotated[str, BeforeValidator(replace_icon)]
    tags: list[str] = []
    awards: list[Award]