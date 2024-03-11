from src.domain.models.food import Food
from src.domain.usecases.food.find import FindFoodParams, IFindFoodUseCase


class FindFoodController:
    def __init__(self, usecase: IFindFoodUseCase):
        self.usecase = usecase

    async def handle(self, id: str, version: str = "global", lang: str = "en") -> Food:
        return await self.usecase.execute(
            FindFoodParams(id=id, version=version, lang=lang)
        )
