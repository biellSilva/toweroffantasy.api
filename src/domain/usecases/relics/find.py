from abc import ABC, abstractmethod

from src.domain.models.relics import Relic
from src.domain.usecases.base import FindParams, IUsecase


class IFindRelicsUseCase(IUsecase[FindParams, Relic], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Relic: ...
