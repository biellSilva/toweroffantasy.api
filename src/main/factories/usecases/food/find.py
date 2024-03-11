from src.data.usecases.food.find import FindFoodUseCase
from src.infra.repository.food.global_ import FoodGlobalRepository


class FindFoodUsecaseFactory:

    @staticmethod
    def create() -> FindFoodUseCase:
        return FindFoodUseCase(FoodGlobalRepository())
