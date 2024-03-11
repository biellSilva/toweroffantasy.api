from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.achievements import Achievement
from src.domain.usecases.achievements.find import (
    FindAchievementsParams,
    IFindAchievementsUseCase,
)
from src.infra.repository.achievements.global_ import AchievementsGlobalRepository


class FindAchievementsUseCase(IFindAchievementsUseCase):
    def __init__(self, repository: AchievementsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindAchievementsParams) -> Achievement:
        if params.version == "global":
            if data := await self.repository.find_by_id(
                **params.model_dump(exclude={"version"})
            ):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
