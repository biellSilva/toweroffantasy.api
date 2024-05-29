from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.mounts import Mount
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.mount.get_all import IGetAllMountUseCase
from src.infra.repository.mounts.global_ import MountsGlobalRepository


class GetAllMountUseCase(IGetAllMountUseCase):
    def __init__(self, repository: MountsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Mount]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
