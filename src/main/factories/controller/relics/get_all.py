from src.main.factories.usecases.relics.get_all import GetAllRelicsUsecaseFactory
from src.presentation.controller.relics.get_all import GetAllRelicsController


class GetAllRelicsControllerFactory:

    @staticmethod
    def create() -> GetAllRelicsController:
        return GetAllRelicsController(GetAllRelicsUsecaseFactory.create())
