from src.domain.errors.http import NotFoundErr
from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    FindSimulacraResult,
    IFindSimulacraUseCase,
)
from src.infra.repository.simulacra import SimulacraRepository


class FindSimulacraUseCase(IFindSimulacraUseCase):
    def __init__(self, repository: SimulacraRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindSimulacraParams) -> FindSimulacraResult:
        if simulacra := await self.repository.find_by_id(**params.model_dump()):
            return FindSimulacraResult(result=simulacra)
        raise NotFoundErr
