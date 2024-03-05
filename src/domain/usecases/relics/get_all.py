
from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.usecases.base import IUsecase


class GetAllRelicsParams(BaseModel):
    ...


class GetAllRelicsResult(BaseModel):
    ...


class IGetAllRelicsUseCase(IUsecase[GetAllRelicsParams, GetAllRelicsResult], ABC):
    @abstractmethod
    async def execute(self, params: GetAllRelicsParams) -> GetAllRelicsResult: ...


