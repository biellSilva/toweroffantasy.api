
from src.data.usecases.relics.get_all import GetAllRelicsUseCase
from src.infra.repository.get_all import GetAllRepository

class GetAllRelicsUsecaseFactory:

    @staticmethod
    def create() -> GetAllRelicsUseCase:
        return GetAllRelicsUseCase(

        )

