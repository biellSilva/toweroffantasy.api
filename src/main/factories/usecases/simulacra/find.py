from src.data.usecases.simulacra.find import FindSimulacraUseCase
from src.infra.repository.simulacra.china import SimulacraChinaRepository
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class FindSimulacraUsecaseFactory:
    @staticmethod
    def create() -> FindSimulacraUseCase:
        return FindSimulacraUseCase(
            SimulacraGlobalRepository(), SimulacraChinaRepository()
        )
