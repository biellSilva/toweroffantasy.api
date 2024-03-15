from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.simulacra.getall import IGetallSimulacraUseCase
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class GetallSimulacraUseCase(IGetallSimulacraUseCase):
    def __init__(self, repository: SimulacraGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Simulacra]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return await filter_models(models, params.filter)
