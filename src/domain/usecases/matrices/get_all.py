from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.matrices import Matrix
from src.domain.usecases.base import IUsecase


class GetAllMatricesParams(BaseModel):
    version: str
    lang: str


class IGetAllMatricesUseCase(IUsecase[GetAllMatricesParams, Matrix], ABC):
    @abstractmethod
    async def execute(self, params: GetAllMatricesParams) -> list[Matrix]: ...
