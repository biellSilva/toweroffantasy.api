
from pydantic import BaseModel, BeforeValidator
from typing import Annotated


class Ingredient(BaseModel):
    matID: Annotated[str, BeforeValidator(lambda x: x.lower())]
    min: Annotated[int, BeforeValidator(lambda x: int(x))]
    max: Annotated[int, BeforeValidator(lambda x: int(x))]