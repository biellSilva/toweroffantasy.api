
from pydantic import BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from api.utils import replace_icon

from .extra import Ingredient


class Food(EntityBase):
    name: str
    # type: str
    description: str
    # satiety: str
    buff: str
    icon: Annotated[str, BeforeValidator(replace_icon)]
    stars: int
    quality: str
    effect: str | None = None
    ingredients: list[Ingredient] = []
    categories: list[str] = []


