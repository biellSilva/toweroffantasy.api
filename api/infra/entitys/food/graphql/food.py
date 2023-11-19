
import strawberry


@strawberry.type
class Ingredient:
    matID: str
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
    quality: str
    effect: str | None
    ingredients: list[Ingredient]
    categories: list[str]

