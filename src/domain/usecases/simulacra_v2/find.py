from abc import ABC, abstractmethod


from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import FindParams, IUsecase


class IFindSimulacraV2UseCase(IUsecase[FindParams, SimulacraV2], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> SimulacraV2: ...
