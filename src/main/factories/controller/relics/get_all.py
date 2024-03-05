
from src.presentation.controller.relics.get_all import GetAllRelicsController
from src.main.factories.usecases.relics.get_all import GetAllRelicsUsecaseFactory

class GetAllRelicsControllerFactory:

    @staticmethod
    def create() -> GetAllRelicsController:
        return GetAllRelicsController(
            GetAllRelicsUsecaseFactory.create()
        )


