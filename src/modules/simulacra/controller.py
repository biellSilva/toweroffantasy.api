from typing import Annotated

from fastapi import Depends, Query

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules._paginator import Pagination
from src.modules.gifts.model import Gift
from src.modules.gifts.repository import GiftsRepository
from src.modules.simulacra.dtos import GetSimulacra, GetSimulacrum
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple
from src.modules.simulacra.repository import ImitationRepository
from src.modules.simulacra.service import ImitationService

router = ApiRouter(prefix="/simulacra", tags=["simulacra"])

SERVICE = ImitationService(ImitationRepository(), GiftsRepository())


@router.get("", response_model=Pagination[SimulacrumSimple])
async def get_simulacra(
    params: Annotated[GetSimulacra, Query()],
) -> Pagination[SimulacrumSimple]:
    return await SERVICE.get_all(params=params)


@router.get(
    "/{simulacrum_id}",
    response_model=Simulacrum,
    exceptions=[SimulacrumNotFoundError(lang=LangsEnum.EN, id="imitation_10")],
)
async def get_simulacrum(params: Annotated[GetSimulacrum, Depends()]) -> Simulacrum:
    return await SERVICE.get(lang=params.lang, _id=params.simulacrum_id)


@router.get(
    "/{simulacrum_id}/gifts",
    response_model=list[Gift],
    exceptions=[SimulacrumNotFoundError(lang=LangsEnum.EN, id="imitation_10")],
)
async def get_simulacrum_liked_gifts(
    params: Annotated[GetSimulacrum, Depends()],
) -> list[Gift]:
    return await SERVICE.get_simulacrum_gifts(
        lang=params.lang,
        _id=params.simulacrum_id,
    )
