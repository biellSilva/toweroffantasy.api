from src.data.usecases.matrices.get_all import GetAllMatricesUseCase
from src.infra.repository.matrices.china import MatricesChinaRepository
from src.infra.repository.matrices.global_ import MatricesGlobalRepository


class GetAllMatricesUsecaseFactory:

    @staticmethod
    def create() -> GetAllMatricesUseCase:
        return GetAllMatricesUseCase(
            MatricesGlobalRepository(), MatricesChinaRepository()
        )
