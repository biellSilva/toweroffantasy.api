from typing import Any
from src.config.include import SIMULACRA_INCLUDE
from src.domain.errors.http import NotFoundErr, NotImplementedErr
from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    IFindSimulacraUseCase,
)
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class FindSimulacraUseCase(IFindSimulacraUseCase):
    def __init__(self, repository: SimulacraGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindSimulacraParams) -> dict[str, Any]:
        if params.version == "global":
            if simulacra := await self.repository.find_by_id(
                **params.model_dump(exclude={"version", "include"})
            ):
                if not params.include:
                    return simulacra.model_dump(include=SIMULACRA_INCLUDE)
                return simulacra.model_dump()

            raise NotFoundErr

        raise NotImplementedErr
