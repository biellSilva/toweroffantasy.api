from typing import TYPE_CHECKING

from src.exceptions.not_found import MatrixSuiteNotFoundError
from src.modules._paginator import Pagination, paginate_items

if TYPE_CHECKING:
    from src._types import LangsEnum
    from src.modules.matrices.dtos import GetMatrices
    from src.modules.matrices.model import Suit
    from src.modules.matrices.repository import MatriceRepository


class MatriceService:
    def __init__(self, matrice_repository: "MatriceRepository") -> None:
        self.matrice_repository = matrice_repository

    async def get(self, *, lang: "LangsEnum", _id: str) -> "Suit":
        if data := await self.matrice_repository.get_id(lang=lang, id_=_id):
            return data
        raise MatrixSuiteNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, params: "GetMatrices") -> "Pagination[Suit]":
        matrices = await self.matrice_repository.get_all(lang=params.lang)

        return paginate_items(matrices, params.page, params.limit)
