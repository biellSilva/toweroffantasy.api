from src.data.usecases.simulacra_v2.get_all import GetAllSimulacraV2UseCase
from src.infra.repository.simulacra_v2.china import SimulacraV2ChinaRepository
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class GetAllSimulacraV2UsecaseFactory:

    @staticmethod
    def create() -> GetAllSimulacraV2UseCase:
        return GetAllSimulacraV2UseCase(
            SimulacraV2GlobalRepository(), SimulacraV2ChinaRepository()
        )
