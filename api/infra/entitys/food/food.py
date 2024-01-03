
from api.infra.entitys.base import EntityBase

from .extra import Ingredient


class Food(EntityBase):
    name: str
    description: str
    buff: str
    icon: str | None
    stars: int
    rarity: int
    effect: str | None = None
    ingredients: list[Ingredient] = []
    categories: list[str] = []


