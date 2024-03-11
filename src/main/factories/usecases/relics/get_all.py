from src.data.usecases.relics.get_all import GetAllRelicsUseCase
from src.infra.repository.relics.global_ import RelicsGlobalRepository


class GetAllRelicsUsecaseFactory:

    @staticmethod
    def create() -> GetAllRelicsUseCase:
        return GetAllRelicsUseCase(RelicsGlobalRepository())
