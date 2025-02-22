from typing import Annotated

from fastapi import Path
from pydantic import BaseModel

from src.modules.base.dtos import BaseSearchDto


class GetMatrix(BaseSearchDto):
    matrix_id: Annotated[str, Path(description="Matrix id")]


class _SuitAssets(BaseModel):
    icon: str
    remould_icon: str
    icon_temp: str


class ExposeSuit(BaseModel):
    id: str
    name: str
    quality: str
    rarity: str
    matrice_name: str
    assets: _SuitAssets
