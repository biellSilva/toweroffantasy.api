
from src.presentation.controller.servants.find import FindServantsController
from src.main.factories.usecases.servants.find import FindServantsUsecaseFactory

class FindServantsControllerFactory:

    @staticmethod
    def create() -> FindServantsController:
        return FindServantsController(
            FindServantsUsecaseFactory.create()
        )


