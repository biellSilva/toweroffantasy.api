
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import bold_numbers


class MatriceSet(BaseModel):
    set_2: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    set_3: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    set_4: Annotated[str, BeforeValidator(bold_numbers)] | None = None


class Matrice(BaseModel):
    name: str
    type: str
    description: Annotated[str, BeforeValidator(bold_numbers)]
    icon: str
    gachaIcon: str
    rarity: str
    set: list[MatriceSet]
    id: str

