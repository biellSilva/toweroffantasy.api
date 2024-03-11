from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.servants import SmartServant
from src.domain.usecases.base import IUsecase


class FindServantsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindServantsUseCase(IUsecase[FindServantsParams, SmartServant], ABC):
    @abstractmethod
    async def execute(self, params: FindServantsParams) -> SmartServant: ...
