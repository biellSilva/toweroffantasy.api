
from pydantic import BaseModel


class Ingredient(BaseModel):
    matID: str
    min: int | str
    max: int | str
