import json

from src.domain.models.achievements import Achievement
from src.domain.usecases.achievements.get_all import (
    GetAllAchievementsParams,
    IGetAllAchievementsUseCase,
)


class GetAllAchievementsController:
    def __init__(self, usecase: IGetAllAchievementsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[Achievement]:
        return await self.usecase.execute(
            GetAllAchievementsParams(
                version=version,
                lang=lang,
                filter=json.loads(filter) if filter else {},
            )
        )
