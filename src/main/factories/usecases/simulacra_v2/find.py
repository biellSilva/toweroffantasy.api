from src.data.usecases.simulacra_v2.find import FindSimulacraV2UseCase
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class FindSimulacraV2UsecaseFactory:

    @staticmethod
    def create() -> FindSimulacraV2UseCase:
        return FindSimulacraV2UseCase(SimulacraV2GlobalRepository())
