from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.simulacra_v2.get_all import IGetAllSimulacraV2UseCase
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class GetAllSimulacraV2UseCase(IGetAllSimulacraV2UseCase):
    def __init__(self, repository: SimulacraV2GlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[SimulacraV2]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return await filter_models(models, params.filter)
