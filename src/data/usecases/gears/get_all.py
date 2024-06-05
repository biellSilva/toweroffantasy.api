from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.gears import Gear
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.gears.get_all import IGetAllGearsUseCase
from src.infra.repository.gears.global_ import GearsGlobalRepository


class GetAllGearsUseCase(IGetAllGearsUseCase):
    def __init__(self, repository: GearsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Gear]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
