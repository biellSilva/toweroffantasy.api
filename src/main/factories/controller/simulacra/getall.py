from src.main.factories.usecases.simulacra.getall import GetallSimulacraUsecaseFactory
from src.presentation.controller.simulacra.getall import GetallSimulacraController


class GetallSimulacraControllerFactory:

    @staticmethod
    def create() -> GetallSimulacraController:
        return GetallSimulacraController(GetallSimulacraUsecaseFactory.create())
