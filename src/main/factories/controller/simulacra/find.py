from src.main.factories.usecases.simulacra.find import FindSimulacraUsecaseFactory
from src.presentation.controller.simulacra.find import FindSimulacraController


class FindSimulacraControllerFactory:

    @staticmethod
    def create() -> FindSimulacraController:
        return FindSimulacraController(FindSimulacraUsecaseFactory.create())
