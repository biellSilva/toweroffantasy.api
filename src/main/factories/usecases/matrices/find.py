from src.data.usecases.matrices.find import FindMatricesUseCase
from src.infra.repository.matrices.global_ import MatricesGlobalRepository


class FindMatricesUsecaseFactory:

    @staticmethod
    def create() -> FindMatricesUseCase:
        return FindMatricesUseCase(MatricesGlobalRepository())
