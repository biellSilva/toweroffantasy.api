from src.main.factories.usecases.simulacra_v2.get_all import (
    GetAllSimulacraV2UsecaseFactory,
)
from src.presentation.controller.simulacra_v2.get_all import GetAllSimulacraV2Controller


class GetAllSimulacraV2ControllerFactory:

    @staticmethod
    def create() -> GetAllSimulacraV2Controller:
        return GetAllSimulacraV2Controller(GetAllSimulacraV2UsecaseFactory.create())
