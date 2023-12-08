
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers, replace_icon


class MatrixSet(BaseModel):
    need: int | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None

class MatrixAssets(BaseModel):
    icon: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='itemIcon')
    iconLarge: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='itemLargeIcon')