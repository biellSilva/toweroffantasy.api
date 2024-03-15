from abc import ABC, abstractmethod

from src.domain.models.matrices import Matrix
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllMatricesUseCase(IUsecase[GetAllParams, Matrix], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Matrix]: ...
