from typing import Annotated

from fastapi import Path
from pydantic import BaseModel

from src.common.dtos import BaseSearchAllDto, BaseSearchDto


class GetMatrix(BaseSearchDto):
    matrix_id: Annotated[str, Path(description="Matrix id")]


class GetMatrices(BaseSearchAllDto):
    include_ids: Annotated[
        list[str] | None,
        Path(description="Matrix id should be one of"),
    ] = None
    exclude_ids: Annotated[
        list[str] | None,
        Path(description="Matrix id should not be one of"),
    ] = None


class _SuitAssets(BaseModel):
    icon: str
    remould_icon: str
    icon_temp: str


class _MatriceAssets(BaseModel):
    icon: str
    large_icon: str


class ExposeSuit(BaseModel):
    id: str
    name: str
    quality: str
    rarity: str
    matrice_name: str
    assets: _SuitAssets
    matrice_assets: _MatriceAssets

    weapon_id: str | None
    imitation_id: str | None
