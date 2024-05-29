from src.decorators.filter import filter_models
from src.domain.errors.http import VersionNotFoundErr
from src.domain.models.relics import Relic
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.relics.get_all import IGetAllRelicsUseCase
from src.infra.repository.relics.china import RelicsChinaRepository
from src.infra.repository.relics.global_ import RelicsGlobalRepository


class GetAllRelicsUseCase(IGetAllRelicsUseCase):
    def __init__(
        self,
        repository: RelicsGlobalRepository,
        china_repository: RelicsChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: GetAllParams) -> list[Relic]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            models = await self.china_repository.get_all(**params.model_dump())

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
