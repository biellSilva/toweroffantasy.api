from src.domain.models.achievements import Achievement
from src.domain.usecases.achievements.get_all import IGetAllAchievementsUseCase
from src.domain.usecases.base import GetAllParams


class GetAllAchievementsController:
    def __init__(self, usecase: IGetAllAchievementsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Achievement]:
        return await self.usecase.execute(
            GetAllParams(
                version=version,
                lang=lang,
                filter=filter,
            )
        )
