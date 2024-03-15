import json
from typing import Any

from fastapi import Depends

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.simulacra.getall import (
    IGetallSimulacraUseCase,
)


class GetallSimulacraController:
    def __init__(self, usecase: IGetallSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[Simulacra] | list[dict[str, Any]]:
        return await self.usecase.execute(
            GetAllParams(
                version=version, lang=lang, filter=json.loads(filter) if filter else None
            )
        )

    async def rest_handle(self, params: GetAllParams = Depends()) -> list[Simulacra]:
        return await self.usecase.execute(params)