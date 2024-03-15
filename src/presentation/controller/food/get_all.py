import json

from src.domain.models.food import Food
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.food.get_all import IGetAllFoodUseCase


class GetAllFoodController:
    def __init__(self, usecase: IGetAllFoodUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Food]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
