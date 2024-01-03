
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import bold_numbers

from api.infra.entitys.base import EntityBase
from api.infra.entitys.banners import Banner
from .extra import MatrixSet, MatrixAssets, MatrixMeta


class Matrix(EntityBase):
    name: str
    simulacrumId: str | None = None
    version: str
    description: Annotated[str, BeforeValidator(bold_numbers)]
    assets: MatrixAssets
    rarity: int
    sets: list[MatrixSet]
    banners: list[Banner] = []
    meta: MatrixMeta
