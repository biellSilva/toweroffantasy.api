

from api.infra.entitys.base import EntityBase

from .extra import Ingredient


class Food(EntityBase):
    name: str
    type: str
    description: str
    satiety: str
    buff: str
    icon: str
    stars: int
    quality: str
    ingredients: list[Ingredient] = []
    mods: list[float] = []


