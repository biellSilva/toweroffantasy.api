from src.decorators.filter import filter_models
from src.domain.errors.http import VersionNotFoundErr
from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.simulacra_v2.get_all import IGetAllSimulacraV2UseCase
from src.infra.repository.simulacra_v2.china import SimulacraV2ChinaRepository
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class GetAllSimulacraV2UseCase(IGetAllSimulacraV2UseCase):
    def __init__(
        self,
        repository: SimulacraV2GlobalRepository,
        china_repository: SimulacraV2ChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: GetAllParams) -> list[SimulacraV2]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            models = await self.china_repository.get_all(**params.model_dump())

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
