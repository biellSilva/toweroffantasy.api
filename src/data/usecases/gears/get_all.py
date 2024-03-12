from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.gears import Gear
from src.domain.usecases.gears.get_all import GetAllGearsParams, IGetAllGearsUseCase
from src.infra.repository.gears.global_ import GearsGlobalRepository


class GetAllGearsUseCase(IGetAllGearsUseCase):
    def __init__(self, repository: GearsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllGearsParams) -> list[Gear]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return filter_models(models, params.filter)
