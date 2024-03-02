import strawberry

from src.domain.models.base import ModelBase
from src.domain.models.food.extra import Ingredient


class Food(ModelBase):
    name: str
    description: str
    buff: str
    icon: str | None
    stars: int
    rarity: int = 1
    effect: str | None = None
    ingredients: list[Ingredient] = []
    categories: list[str] = []


@strawberry.experimental.pydantic.type(model=Food, all_fields=True)
class FoodType:
    pass
