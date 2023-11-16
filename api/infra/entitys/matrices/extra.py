
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import bold_numbers


class MatrixSet(BaseModel):
    need: int | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None
