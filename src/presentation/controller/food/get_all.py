import json

from src.domain.models.food import Food
from src.domain.usecases.food.get_all import GetAllFoodParams, IGetAllFoodUseCase


class GetAllFoodController:
    def __init__(self, usecase: IGetAllFoodUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[Food]:
        return await self.usecase.execute(
            GetAllFoodParams(
                version=version, lang=lang, filter=json.loads(filter) if filter else {}
            )
        )
