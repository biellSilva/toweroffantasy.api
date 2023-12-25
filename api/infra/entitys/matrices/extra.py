
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers


class MatrixSet(BaseModel):
    need: int | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None

class MatrixAssets(BaseModel):
    icon: str | None = Field(alias='itemIcon')
    iconLarge: str | None = Field(alias='itemLargeIcon')
    characterArtwork: str | None = None