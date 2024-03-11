
from src.presentation.controller.food.get_all import GetAllFoodController
from src.main.factories.usecases.food.get_all import GetAllFoodUsecaseFactory

class GetAllFoodControllerFactory:

    @staticmethod
    def create() -> GetAllFoodController:
        return GetAllFoodController(
            GetAllFoodUsecaseFactory.create()
        )


