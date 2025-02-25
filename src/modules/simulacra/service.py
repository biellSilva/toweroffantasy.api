from typing import TYPE_CHECKING

from src._types import LangsEnum
from src._utils import paginate_items
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules.simulacra.dtos import GetSimulacra
from src.modules.simulacra.utils import filter_simulacra

if TYPE_CHECKING:
    from src.modules.simulacra.model import Simulacrum, SimulacrumSimple
    from src.modules.simulacra.repository import ImitationRepository


class ImitationService:
    def __init__(self, repository: "ImitationRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: LangsEnum, _id: str) -> "Simulacrum":
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return data
        raise SimulacrumNotFoundError(lang=lang, id=_id)

    async def get_all(
        self,
        *,
        params: GetSimulacra,
        include_id: list[str] | None,
        exclude_id: list[str] | None,
        include_sex: list[str] | None,
        exclude_sex: list[str] | None,
        include_rarity: list[str] | None,
        exclude_rarity: list[str] | None,
    ) -> "list[SimulacrumSimple]":
        simulacra = await self.repository.get_all(lang=params.lang)

        filtered = [
            data
            for data in simulacra
            if filter_simulacra(
                data,
                params=params,
                include_id=include_id,
                exclude_id=exclude_id,
                include_sex=include_sex,
                exclude_sex=exclude_sex,
                include_rarity=include_rarity,
                exclude_rarity=exclude_rarity,
            )
        ]

        return paginate_items(filtered, params.page, params.limit)
