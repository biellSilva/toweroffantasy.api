import json

from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.simulacra_v2.get_all import (
    GetAllSimulacraV2Params,
    IGetAllSimulacraV2UseCase,
)


class GetAllSimulacraV2Controller:
    def __init__(self, usecase: IGetAllSimulacraV2UseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[SimulacraV2]:
        return await self.usecase.execute(
            GetAllSimulacraV2Params(
                version=version, lang=lang, filter=json.loads(filter) if filter else {}
            )
        )
