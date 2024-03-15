from abc import ABC, abstractmethod

from src.domain.models.relics import Relic
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllRelicsUseCase(IUsecase[GetAllParams, Relic], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Relic]: ...
