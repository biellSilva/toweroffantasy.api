
from pydantic import BaseModel, BeforeValidator
from typing import Annotated


class Ingredient(BaseModel):
    matID: Annotated[str, BeforeValidator(lambda x: x.lower())]
    min: int | str
    max: int | str