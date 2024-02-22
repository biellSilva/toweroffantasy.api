from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.infra.entitys.item.item import Item


class Ingredient(BaseModel):
    matID: Item
    min: Annotated[int, BeforeValidator(lambda x: int(x))]
    max: Annotated[int, BeforeValidator(lambda x: int(x))]
