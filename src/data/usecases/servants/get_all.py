from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.servants import SmartServant
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.servants.get_all import (
    IGetAllServantsUseCase,
)
from src.infra.repository.servants.global_ import SmartServantsGlobalRepository


class GetAllServantsUseCase(IGetAllServantsUseCase):
    def __init__(self, repository: SmartServantsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[SmartServant]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return await filter_models(models, params.filter)
