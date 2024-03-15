from abc import ABC, abstractmethod

from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllSimulacraV2UseCase(IUsecase[GetAllParams, SimulacraV2], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[SimulacraV2]: ...
