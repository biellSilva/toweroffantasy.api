from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.achievements import Achievement
from src.domain.usecases.achievements.get_all import (
    GetAllAchievementsParams,
    IGetAllAchievementsUseCase,
)
from src.infra.repository.achievements.global_ import AchievementsGlobalRepository


class GetAllAchievementsUseCase(IGetAllAchievementsUseCase):
    def __init__(self, repository: AchievementsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllAchievementsParams) -> list[Achievement]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
