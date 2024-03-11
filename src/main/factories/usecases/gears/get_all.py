from src.data.usecases.gears.get_all import GetAllGearsUseCase
from src.infra.repository.gears.global_ import GearsGlobalRepository


class GetAllGearsUsecaseFactory:

    @staticmethod
    def create() -> GetAllGearsUseCase:
        return GetAllGearsUseCase(GearsGlobalRepository())
