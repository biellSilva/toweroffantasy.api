from src.main.factories.usecases.food.get_all import GetAllFoodUsecaseFactory
from src.presentation.controller.food.get_all import GetAllFoodController


class GetAllFoodControllerFactory:

    @staticmethod
    def create() -> GetAllFoodController:
        return GetAllFoodController(GetAllFoodUsecaseFactory.create())
