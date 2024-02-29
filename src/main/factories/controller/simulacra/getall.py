
from src.presentation.controller.simulacra.getall import GetallSimulacraController
from src.main.factories.usecases.simulacra.getall import GetallSimulacraUsecaseFactory

class GetallSimulacraControllerFactory:

    @staticmethod
    def create() -> GetallSimulacraController:
        return GetallSimulacraController(
            GetallSimulacraUsecaseFactory.create()
        )


