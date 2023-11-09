
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers


class MatriceSet(BaseModel):
    set_2: Annotated[str, BeforeValidator(bold_numbers)] | None = Field(default=None, alias='2', serialization_alias='set_2')
    set_4: Annotated[str, BeforeValidator(bold_numbers)] | None = Field(default=None, alias='4', serialization_alias='set_4')
