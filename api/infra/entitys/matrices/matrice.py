
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import bold_numbers

from api.infra.entitys.base import EntityBase
from api.infra.entitys.matrices.extra import MatriceSet


class Matrice(EntityBase):
    name: str
    type: str
    description: Annotated[str, BeforeValidator(bold_numbers)]
    icon: str
    gachaIcon: str
    rarity: str
    set: MatriceSet
