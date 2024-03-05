from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.matrices import Matrix
from src.domain.usecases.base import IUsecase


class FindMatricesParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindMatricesUseCase(IUsecase[FindMatricesParams, Matrix], ABC):
    @abstractmethod
    async def execute(self, params: FindMatricesParams) -> Matrix: ...
