
from src.domain.usecases.relics.get_all import GetAllRelicsParams, GetAllRelicsResult, IGetAllRelicsUseCase


class GetAllRelicsController:
    def __init__(self, usecase: IGetAllRelicsUseCase):
        self.usecase = usecase

    async def handle(self, params: GetAllRelicsParams) -> GetAllRelicsResult:
        return await self.usecase.execute(params)


