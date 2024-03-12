from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.relics import Relic
from src.domain.usecases.relics.get_all import GetAllRelicsParams, IGetAllRelicsUseCase
from src.infra.repository.relics.global_ import RelicsGlobalRepository


class GetAllRelicsUseCase(IGetAllRelicsUseCase):
    def __init__(self, repository: RelicsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllRelicsParams) -> list[Relic]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return filter_models(models, params.filter)
