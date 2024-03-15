from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.achievements import Achievement
from src.domain.usecases.achievements.get_all import (
    IGetAllAchievementsUseCase,
)
from src.domain.usecases.base import GetAllParams
from src.infra.repository.achievements.global_ import AchievementsGlobalRepository


class GetAllAchievementsUseCase(IGetAllAchievementsUseCase):
    def __init__(self, repository: AchievementsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Achievement]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return await filter_models(models=models, filter_str=params.filter)
