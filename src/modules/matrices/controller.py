from typing import Annotated

from fastapi import Depends

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import MatrixSuiteNotFoundError
from src.modules.base.dtos import BaseSearchDto
from src.modules.matrices.dtos import GetMatrix
from src.modules.matrices.model import Suit
from src.modules.matrices.repository import MatriceRepository
from src.modules.matrices.service import MatriceService

router = ApiRouter(prefix="/matrices", tags=["matrices"])

SERVICE = MatriceService(MatriceRepository())


@router.get("", response_model=list[Suit])
async def get_all_matrice(params: Annotated[BaseSearchDto, Depends()]) -> list[Suit]:
    return await SERVICE.get_all(lang=params.lang)


@router.get(
    "/{matrix_id}",
    response_model=Suit,
    exceptions=[MatrixSuiteNotFoundError(lang=LangsEnum.EN, id="suit_SSR1")],
)
async def get_matrice(params: Annotated[GetMatrix, Depends()]) -> Suit:
    return await SERVICE.get(lang=params.lang, _id=params.matrix_id)
