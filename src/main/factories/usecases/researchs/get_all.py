from src.data.usecases.researchs.get_all import GetAllResearchsUseCase
from src.infra.repository.researchs.global_ import ResearchsGlobalRepository


class GetAllResearchsUsecaseFactory:

    @staticmethod
    def create() -> GetAllResearchsUseCase:
        return GetAllResearchsUseCase(ResearchsGlobalRepository())
