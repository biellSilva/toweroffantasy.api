
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import bold_numbers, replace_icon

from api.infra.entitys.base import EntityBase
from api.infra.entitys.matrices.extra import MatrixSet


class Matrix(EntityBase):
    name: str
    type: str
    description: Annotated[str, BeforeValidator(bold_numbers)]
    icon: Annotated[str, BeforeValidator(replace_icon)]
    # gachaIcon: str
    rarity: str
    set: MatrixSet

