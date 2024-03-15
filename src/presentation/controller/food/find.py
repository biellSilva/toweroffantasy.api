from src.domain.models.food import Food
from src.domain.usecases.base import FindParams
from src.domain.usecases.food.find import IFindFoodUseCase


class FindFoodController:
    def __init__(self, usecase: IFindFoodUseCase):
        self.usecase = usecase

    async def handle(self, id: str, version: str = "global", lang: str = "en") -> Food:
        return await self.usecase.execute(FindParams(id=id, version=version, lang=lang))
