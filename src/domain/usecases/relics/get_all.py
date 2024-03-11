from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.relics import Relic

from src.domain.usecases.base import IUsecase


class GetAllRelicsParams(BaseModel):
    version: str
    lang: str


class IGetAllRelicsUseCase(IUsecase[GetAllRelicsParams, Relic], ABC):
    @abstractmethod
    async def execute(self, params: GetAllRelicsParams) -> list[Relic]: ...
