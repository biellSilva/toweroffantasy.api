from src.data.usecases.guidebooks.get_all import GetAllGuidebooksUseCase
from src.infra.repository.guidebooks.global_ import GuidebooksGlobalRepository


class GetAllGuidebooksUsecaseFactory:

    @staticmethod
    def create() -> GetAllGuidebooksUseCase:
        return GetAllGuidebooksUseCase(GuidebooksGlobalRepository())
