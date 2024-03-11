from src.main.factories.usecases.simulacra_v2.find import FindSimulacraV2UsecaseFactory
from src.presentation.controller.simulacra_v2.find import FindSimulacraV2Controller


class FindSimulacraV2ControllerFactory:

    @staticmethod
    def create() -> FindSimulacraV2Controller:
        return FindSimulacraV2Controller(FindSimulacraV2UsecaseFactory.create())
