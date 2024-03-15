from abc import ABC, abstractmethod

from src.domain.models.items import Item
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllItemsUseCase(IUsecase[GetAllParams, Item], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Item]: ...
