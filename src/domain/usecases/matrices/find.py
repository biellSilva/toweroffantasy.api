from abc import ABC, abstractmethod

from src.domain.models.matrices import Matrix
from src.domain.usecases.base import FindParams, IUsecase


class IFindMatricesUseCase(IUsecase[FindParams, Matrix], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Matrix: ...
