from typing import Any

from src.config.include import SIMULACRA_INCLUDE
from src.domain.errors.http import NotImplementedErr
from src.domain.usecases.simulacra.getall import (
    GetallSimulacraParams,
    IGetallSimulacraUseCase,
)
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class GetallSimulacraUseCase(IGetallSimulacraUseCase):
    def __init__(self, repository: SimulacraGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetallSimulacraParams) -> list[dict[str, Any]]:
        if params.version == "global":
            if not params.include:
                return [
                    data.model_dump(include=SIMULACRA_INCLUDE)
                    for data in await self.repository.get_all(
                        **params.model_dump(exclude={"version", "include"})
                    )
                ]
            return [
                data.model_dump()
                for data in await self.repository.get_all(
                    **params.model_dump(exclude={"version", "include"})
                )
            ]

        raise NotImplementedErr
