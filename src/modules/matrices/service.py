from typing import TYPE_CHECKING

from src.exceptions.not_found import MatrixSuiteNotFoundError
from src.modules._paginator import Pagination

if TYPE_CHECKING:
    from src.modules.matrices.dtos import GetMatrices, GetMatrix
    from src.modules.matrices.model import Suit
    from src.modules.matrices.repository import MatriceRepository


class MatriceService:
    def __init__(self, matrice_repository: "MatriceRepository") -> None:
        self.matrice_repository = matrice_repository

    async def get(self, params: "GetMatrix") -> "Suit":
        if data := await self.matrice_repository.get_matrix(params):
            return data
        raise MatrixSuiteNotFoundError(**params.model_dump(mode="json"))

    async def get_all(self, *, params: "GetMatrices") -> "Pagination[Suit]":
        count = await self.matrice_repository.count_matrices(params)
        matrices = await self.matrice_repository.get_matrices(params)

        return Pagination(
            data=matrices,
            total_items=count,
            page=params.page,
            limit=params.limit,
            max_page=count // params.limit + 1,
        )
