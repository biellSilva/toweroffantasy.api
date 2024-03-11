from src.data.usecases.servants.find import FindServantsUseCase
from src.infra.repository.servants.global_ import SmartServantsGlobalRepository


class FindServantsUsecaseFactory:

    @staticmethod
    def create() -> FindServantsUseCase:
        return FindServantsUseCase(SmartServantsGlobalRepository())
