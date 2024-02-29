
from src.domain.errors.http import NotImplementedErr
from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.getall import GetallSimulacraParams, IGetallSimulacraUseCase
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class GetallSimulacraUseCase(IGetallSimulacraUseCase):
    def __init__(self, repository: SimulacraGlobalRepository) -> None:
        self.repository = repository

        
    async def execute(self, params: GetallSimulacraParams) -> list[Simulacra]:
        if params.version == 'global':
            return await self.repository.get_all(**params.model_dump(exclude={'version'}))
        
        raise NotImplementedErr



