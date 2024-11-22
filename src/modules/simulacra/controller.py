from typing import Annotated

from fastapi import Depends

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules.base.dtos import BaseDataDto
from src.modules.simulacra.dtos import GetImitation
from src.modules.simulacra.model import Imitation
from src.modules.simulacra.repository import ImitationRepository
from src.modules.simulacra.service import ImitationService

router = ApiRouter(prefix="/simulacra", tags=["simulacra"])

SERVICE = ImitationService(ImitationRepository())


@router.get("", response_model=list[Imitation])
async def get_all_simulacra(
    params: Annotated[BaseDataDto, Depends()],
) -> list[Imitation]:
    return await SERVICE.get_all(lang=params.lang)


@router.get(
    "/{imitation_id}",
    response_model=Imitation,
    exceptions=[SimulacrumNotFoundError(lang=LangsEnum.EN, id="imitation_10")],
)
async def get_simulacrum(params: Annotated[GetImitation, Depends()]) -> Imitation:
    return await SERVICE.get(lang=params.lang, _id=params.imitation_id)
