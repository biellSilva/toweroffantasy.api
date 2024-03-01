from typing import Any

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    IFindSimulacraUseCase,
)


class FindSimulacraController:
    def __init__(self, usecase: IFindSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Simulacra | dict[str, Any]:

        return await self.usecase.execute(
            FindSimulacraParams(id=id, version=version, lang=lang)
        )
