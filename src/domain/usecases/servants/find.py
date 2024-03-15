from abc import ABC, abstractmethod

from src.domain.models.servants import SmartServant
from src.domain.usecases.base import FindParams, IUsecase


class IFindServantsUseCase(IUsecase[FindParams, SmartServant], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> SmartServant: ...
