from typing import Annotated

from fastapi import Depends

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import MatrixSuiteNotFoundError
from src.modules._paginator import Pagination
from src.modules.matrices.dtos import ExposeSuit, GetMatrices, GetMatrix
from src.modules.matrices.model import Suit
from src.modules.matrices.repository import MatriceRepository
from src.modules.matrices.service import MatriceService

router = ApiRouter(prefix="/matrices", tags=["matrices"])

SERVICE = MatriceService(MatriceRepository())


@router.get("", response_model=Pagination[ExposeSuit])
async def get_all_matrice(
    params: Annotated[GetMatrices, Depends()],
) -> Pagination[Suit]:
    return await SERVICE.get_all(params=params)


@router.get(
    "/{matrix_id}",
    response_model=Suit,
    exceptions=[MatrixSuiteNotFoundError(lang=LangsEnum.EN, id="suit_SSR1")],
)
async def get_matrice(params: Annotated[GetMatrix, Depends()]) -> Suit:
    return await SERVICE.get(lang=params.lang, _id=params.matrix_id)
