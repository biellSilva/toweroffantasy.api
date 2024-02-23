from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    FindSimulacraResult,
    IFindSimulacraUseCase,
)


class FindSimulacraController:
    def __init__(self, usecase: IFindSimulacraUseCase):
        self.usecase = usecase

    async def handle(self, params: FindSimulacraParams) -> FindSimulacraResult:
        "Find simulacra based on ID"
        return await self.usecase.execute(params)
