from typing import TYPE_CHECKING

from src._types import LangsEnum
from src.exceptions.not_found import MatrixSuiteNotFoundError
from src.modules.matrices.model import Suit

if TYPE_CHECKING:
    from src.modules.matrices.repository import MatriceRepository


class MatriceService:
    def __init__(self, matrice_repository: "MatriceRepository") -> None:
        self.matrice_repository = matrice_repository

    async def get(self, *, lang: LangsEnum, _id: str) -> Suit:
        if data := await self.matrice_repository.get_id(lang=lang, _id=_id):
            return Suit(**data)
        raise MatrixSuiteNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, lang: LangsEnum) -> list[Suit]:
        return [
            Suit(**data) for data in await self.matrice_repository.get_all(lang=lang)
        ]
