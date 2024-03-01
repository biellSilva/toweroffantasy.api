from typing import Any

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.getall import (
    GetallSimulacraParams,
    IGetallSimulacraUseCase,
)


class GetallSimulacraController:
    def __init__(self, usecase: IGetallSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en"
    ) -> list[Simulacra] | list[dict[str, Any]]:
        return await self.usecase.execute(
            GetallSimulacraParams(version=version, lang=lang)
        )
