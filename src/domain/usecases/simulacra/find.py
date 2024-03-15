from abc import ABC, abstractmethod

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import FindParams, IUsecase


class IFindSimulacraUseCase(IUsecase[FindParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Simulacra: ...
