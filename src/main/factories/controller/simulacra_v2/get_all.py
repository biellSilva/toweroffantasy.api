
from src.presentation.controller.simulacra_v2.get_all import GetAllSimulacraV2Controller
from src.main.factories.usecases.simulacra_v2.get_all import GetAllSimulacraV2UsecaseFactory

class GetAllSimulacraV2ControllerFactory:

    @staticmethod
    def create() -> GetAllSimulacraV2Controller:
        return GetAllSimulacraV2Controller(
            GetAllSimulacraV2UsecaseFactory.create()
        )


