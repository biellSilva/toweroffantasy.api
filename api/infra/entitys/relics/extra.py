
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers


class Advancement(BaseModel):
    id: str = Field(exclude=True)
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = Field(default=None, exclude=True)
