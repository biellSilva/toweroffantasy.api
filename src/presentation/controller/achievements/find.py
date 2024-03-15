from src.domain.models.achievements import Achievement
from src.domain.usecases.achievements.find import (
    IFindAchievementsUseCase,
)
from src.domain.usecases.base import FindParams


class FindAchievementsController:
    def __init__(self, usecase: IFindAchievementsUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Achievement:
        return await self.usecase.execute(
            FindParams(id=id, version=version, lang=lang)
        )
