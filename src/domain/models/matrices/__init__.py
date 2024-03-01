from typing import Annotated

from pydantic import AliasChoices, BeforeValidator, Field
import strawberry

from src.domain.models.banner import Banner
from src.domain.models.base import ModelBase
from src.domain.models.matrices.extra import MatrixAsset, MatrixMeta, MatrixSet
from src.utils import bold_numbers


class Matrix(ModelBase):
    name: str
    description: Annotated[str, BeforeValidator(bold_numbers)]
    assets: MatrixAsset
    rarity: int
    sets: list[MatrixSet] = Field(validation_alias=AliasChoices("sets", "set"))
    version: str
    weaponId: str | None
    simulacrumId: str | None = None
    banners: list[Banner] = []
    meta: MatrixMeta


@strawberry.experimental.pydantic.type(model=Matrix, all_fields=True)
class MatrixType:
    pass
