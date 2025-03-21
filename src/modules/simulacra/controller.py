from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.modules._paginator import Pagination
from src.modules.gifts.model import Gift
from src.modules.gifts.repository import GiftsRepository
from src.modules.simulacra.dtos import GetSimulacra, GetSimulacrum
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple
from src.modules.simulacra.repository import ImitationRepository
from src.modules.simulacra.service import ImitationService

router = APIRouter(prefix="/simulacra", tags=["simulacra"])

SERVICE = ImitationService(ImitationRepository(), GiftsRepository())


@router.get("")
async def get_simulacra(
    params: Annotated[GetSimulacra, Query()],
) -> Pagination[SimulacrumSimple]:
    return await SERVICE.get_all(params=params)


@router.get("/{simulacrum_id}")
async def get_simulacrum(params: Annotated[GetSimulacrum, Depends()]) -> Simulacrum:
    return await SERVICE.get(lang=params.lang, _id=params.simulacrum_id)


@router.get("/{simulacrum_id}/gifts")
async def get_simulacrum_liked_gifts(
    params: Annotated[GetSimulacrum, Depends()],
) -> list[Gift]:
    return await SERVICE.get_simulacrum_gifts(
        lang=params.lang,
        _id=params.simulacrum_id,
    )
