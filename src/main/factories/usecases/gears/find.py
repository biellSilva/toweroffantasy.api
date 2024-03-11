from src.data.usecases.gears.find import FindGearsUseCase
from src.infra.repository.gears.global_ import GearsGlobalRepository


class FindGearsUsecaseFactory:

    @staticmethod
    def create() -> FindGearsUseCase:
        return FindGearsUseCase(GearsGlobalRepository())
