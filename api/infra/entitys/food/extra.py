
from pydantic import BaseModel

from api.infra.entitys.item import Item


class Ingredient(BaseModel):
    matID: str
    min: int | str
    max: int | str
    item: Item | None = None