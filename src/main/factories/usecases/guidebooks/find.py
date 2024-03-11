from src.data.usecases.guidebooks.find import FindGuidebooksUseCase
from src.infra.repository.guidebooks.global_ import GuidebooksGlobalRepository


class FindGuidebooksUsecaseFactory:

    @staticmethod
    def create() -> FindGuidebooksUseCase:
        return FindGuidebooksUseCase(GuidebooksGlobalRepository())
