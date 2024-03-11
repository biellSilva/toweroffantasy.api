from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.simulacra_v2.find import (
    FindSimulacraV2Params,
    IFindSimulacraV2UseCase,
)


class FindSimulacraV2Controller:
    def __init__(self, usecase: IFindSimulacraV2UseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> SimulacraV2:
        return await self.usecase.execute(
            FindSimulacraV2Params(id=id, version=version, lang=lang)
        )
