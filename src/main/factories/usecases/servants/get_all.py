from src.data.usecases.servants.get_all import GetAllServantsUseCase
from src.infra.repository.servants.global_ import SmartServantsGlobalRepository


class GetAllServantsUsecaseFactory:

    @staticmethod
    def create() -> GetAllServantsUseCase:
        return GetAllServantsUseCase(SmartServantsGlobalRepository())
