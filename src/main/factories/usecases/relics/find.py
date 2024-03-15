from src.data.usecases.relics.find import FindRelicsUseCase
from src.infra.repository.relics.china import RelicsChinaRepository
from src.infra.repository.relics.global_ import RelicsGlobalRepository


class FindRelicsUsecaseFactory:

    @staticmethod
    def create() -> FindRelicsUseCase:
        return FindRelicsUseCase(RelicsGlobalRepository(), RelicsChinaRepository())
