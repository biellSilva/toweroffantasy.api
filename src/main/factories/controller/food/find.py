
from src.presentation.controller.food.find import FindFoodController
from src.main.factories.usecases.food.find import FindFoodUsecaseFactory

class FindFoodControllerFactory:

    @staticmethod
    def create() -> FindFoodController:
        return FindFoodController(
            FindFoodUsecaseFactory.create()
        )


