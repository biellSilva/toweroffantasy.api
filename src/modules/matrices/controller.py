from typing import Annotated

from fastapi import APIRouter, Query

from src.modules._paginator import Pagination
from src.modules.matrices.dtos import ExposeSuit, GetMatrices, GetMatrix
from src.modules.matrices.model import Suit
from src.modules.matrices.repository import MatriceRepository
from src.modules.matrices.service import MatriceService

router = APIRouter(prefix="/matrices", tags=["matrices"])

SERVICE = MatriceService(MatriceRepository())


@router.get("", response_model=Pagination[ExposeSuit])
async def get_all_matrice(
    params: Annotated[GetMatrices, Query()],
) -> Pagination[Suit]:
    return await SERVICE.get_all(params=params)


@router.get("/{matrix_id}")
async def get_matrice(params: Annotated[GetMatrix, Query()]) -> Suit:
    return await SERVICE.get(params)
