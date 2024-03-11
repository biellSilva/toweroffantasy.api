from src.main.factories.usecases.servants.find import FindServantsUsecaseFactory
from src.presentation.controller.servants.find import FindServantsController


class FindServantsControllerFactory:

    @staticmethod
    def create() -> FindServantsController:
        return FindServantsController(FindServantsUsecaseFactory.create())
