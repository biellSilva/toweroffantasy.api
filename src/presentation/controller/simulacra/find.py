from typing import Any
from fastapi import Depends

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    IFindSimulacraUseCase,
)


class FindSimulacraController:
    def __init__(self, usecase: IFindSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self,
        params: FindSimulacraParams = Depends(),
    ) -> Simulacra | dict[str, Any]:
        "Find simulacra based on ID"
        return await self.usecase.execute(params)
