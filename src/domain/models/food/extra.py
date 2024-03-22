from typing import Annotated

import strawberry
from pydantic import BaseModel, BeforeValidator

from src.domain.models.items import Item


class Ingredient(BaseModel):
    matID: Item
    min: Annotated[int, BeforeValidator(lambda x: int(x))]
    max: Annotated[int, BeforeValidator(lambda x: int(x))]
    source: list[str]


@strawberry.experimental.pydantic.type(model=Ingredient, all_fields=True)
class IngredientType:
    pass
