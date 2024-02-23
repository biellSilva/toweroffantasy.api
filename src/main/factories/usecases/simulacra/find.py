from src.data.usecases.simulacra.find import FindSimulacraUseCase
from src.infra.repository.simulacra import SimulacraRepository


class FindSimulacraUsecaseFactory:
    @staticmethod
    def create() -> FindSimulacraUseCase:
        return FindSimulacraUseCase(SimulacraRepository())
