from typing import Any

from fastapi import Depends

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.getall import (
    GetallSimulacraParams,
    IGetallSimulacraUseCase,
)


class GetallSimulacraController:
    def __init__(self, usecase: IGetallSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self,
        params: GetallSimulacraParams = Depends(),
    ) -> list[Simulacra] | list[dict[str, Any]]:
        return await self.usecase.execute(params)
