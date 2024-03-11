from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import IUsecase


class GetAllSimulacraV2Params(BaseModel):
    version: str
    lang: str


class IGetAllSimulacraV2UseCase(IUsecase[GetAllSimulacraV2Params, SimulacraV2], ABC):
    @abstractmethod
    async def execute(self, params: GetAllSimulacraV2Params) -> list[SimulacraV2]: ...
