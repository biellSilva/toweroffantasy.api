
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import bold_numbers, replace_icon


class Advancement(BaseModel):
    id: Annotated[str, BeforeValidator(replace_icon)]
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
