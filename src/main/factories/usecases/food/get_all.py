from src.data.usecases.food.get_all import GetAllFoodUseCase
from src.infra.repository.food.global_ import FoodGlobalRepository


class GetAllFoodUsecaseFactory:

    @staticmethod
    def create() -> GetAllFoodUseCase:
        return GetAllFoodUseCase(FoodGlobalRepository())
