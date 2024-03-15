from src.data.usecases.researchs.find import FindResearchsUseCase
from src.infra.repository.researchs.global_ import ResearchsGlobalRepository


class FindResearchsUsecaseFactory:

    @staticmethod
    def create() -> FindResearchsUseCase:
        return FindResearchsUseCase(ResearchsGlobalRepository())
