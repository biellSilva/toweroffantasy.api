from typing import Annotated
from pydantic import BaseModel, BeforeValidator

from src.domain.models.items import Item


class Ingredient(BaseModel):
    matID: Item
    min: Annotated[int, BeforeValidator(lambda x: int(x))]
    max: Annotated[int, BeforeValidator(lambda x: int(x))]
