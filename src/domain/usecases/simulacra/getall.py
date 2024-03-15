from abc import ABC, abstractmethod

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetallSimulacraUseCase(IUsecase[GetAllParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Simulacra]: ...
