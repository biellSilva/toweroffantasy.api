from abc import ABC, abstractmethod

from src.domain.models.items import Item
from src.domain.usecases.base import FindParams, IUsecase

class IFindItemsUseCase(IUsecase[FindParams, Item], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Item: ...
