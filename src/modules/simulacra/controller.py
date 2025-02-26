from typing import Annotated

from fastapi import Depends, Query

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules.gifts.model import Gift
from src.modules.gifts.repository import GiftsRepository
from src.modules.simulacra.dtos import GetSimulacra, GetSimulacrum
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple
from src.modules.simulacra.repository import ImitationRepository
from src.modules.simulacra.service import ImitationService

router = ApiRouter(prefix="/simulacra", tags=["simulacra"])

SERVICE = ImitationService(ImitationRepository(), GiftsRepository())


@router.get("", response_model=list[SimulacrumSimple])
async def get_simulacra(
    params: Annotated[GetSimulacra, Depends()],
    include_ids: Annotated[
        list[str] | None,
        Query(description="Id should be one of"),
    ] = None,
    exclude_ids: Annotated[
        list[str] | None,
        Query(description="Id should not be one of"),
    ] = None,
    include_sex: Annotated[
        list[str] | None,
        Query(description="Sex should include one of"),
    ] = None,
    exclude_sex: Annotated[
        list[str] | None,
        Query(description="Sex should exclude one of"),
    ] = None,
    include_rarities: Annotated[
        list[str] | None,
        Query(description="Rarity should include one of"),
    ] = None,
    exclude_rarities: Annotated[
        list[str] | None,
        Query(description="Rarity should exclude one of"),
    ] = None,
) -> list[SimulacrumSimple]:
    return await SERVICE.get_all(
        params=params,
        include_id=include_ids,
        exclude_id=exclude_ids,
        include_sex=include_sex,
        include_rarity=include_rarities,
        exclude_rarity=exclude_rarities,
        exclude_sex=exclude_sex,
    )


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
