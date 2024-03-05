from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.relics import Relic

from src.domain.usecases.base import IUsecase


class FindRelicsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindRelicsUseCase(IUsecase[FindRelicsParams, Relic], ABC):
    @abstractmethod
    async def execute(self, params: FindRelicsParams) -> Relic: ...
