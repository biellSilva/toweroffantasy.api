from src.data.usecases.simulacra.getall import GetallSimulacraUseCase
from src.infra.repository.simulacra.china import SimulacraChinaRepository
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class GetallSimulacraUsecaseFactory:

    @staticmethod
    def create() -> GetallSimulacraUseCase:
        return GetallSimulacraUseCase(
            SimulacraGlobalRepository(), SimulacraChinaRepository()
        )
