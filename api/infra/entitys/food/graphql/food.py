import strawberry

from api.infra.entitys.item.graphql.item import Item


@strawberry.type
class Ingredient:
    matID: Item
    min: str
    max: str


@strawberry.type
class Food:
    id: str
    name: str
    description: str
    buff: str
    icon: str
    stars: int
    rarity: int
    effect: str | None
    ingredients: list[Ingredient]
    categories: list[str]
