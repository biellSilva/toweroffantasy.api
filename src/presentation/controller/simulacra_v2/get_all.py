import json

from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.simulacra_v2.get_all import (
    IGetAllSimulacraV2UseCase,
)


class GetAllSimulacraV2Controller:
    def __init__(self, usecase: IGetAllSimulacraV2UseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[SimulacraV2]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
