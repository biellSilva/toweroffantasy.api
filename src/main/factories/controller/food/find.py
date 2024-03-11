from src.main.factories.usecases.food.find import FindFoodUsecaseFactory
from src.presentation.controller.food.find import FindFoodController


class FindFoodControllerFactory:

    @staticmethod
    def create() -> FindFoodController:
        return FindFoodController(FindFoodUsecaseFactory.create())
