
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import bold_numbers

from api.infra.entitys.base import EntityBase
from api.infra.entitys.banners import Banner
from .extra import MatrixSet, MatrixAssets


class Matrix(EntityBase):
    name: str
    type: str
    description: Annotated[str, BeforeValidator(bold_numbers)]
    assets: MatrixAssets
    rarity: str
    sets: list[MatrixSet]
    Banners: list[Banner]

