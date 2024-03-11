from src.main.factories.usecases.relics.find import FindRelicsUsecaseFactory
from src.presentation.controller.relics.find import FindRelicsController


class FindRelicsControllerFactory:

    @staticmethod
    def create() -> FindRelicsController:
        return FindRelicsController(FindRelicsUsecaseFactory.create())
