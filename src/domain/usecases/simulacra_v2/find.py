from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import IUsecase


class FindSimulacraV2Params(BaseModel):
    id: str
    version: str
    lang: str


class IFindSimulacraV2UseCase(IUsecase[FindSimulacraV2Params, SimulacraV2], ABC):
    @abstractmethod
    async def execute(self, params: FindSimulacraV2Params) -> SimulacraV2: ...
