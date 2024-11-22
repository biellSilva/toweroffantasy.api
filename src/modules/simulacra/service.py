from typing import TYPE_CHECKING

from src._types import LangsEnum
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules.simulacra.model import Imitation

if TYPE_CHECKING:
    from src.modules.simulacra.repository import ImitationRepository


class ImitationService:
    def __init__(self, repository: "ImitationRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: LangsEnum, _id: str) -> Imitation:
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return Imitation(**data)
        raise SimulacrumNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, lang: LangsEnum) -> list[Imitation]:
        return [Imitation(**data) for data in await self.repository.get_all(lang=lang)]
