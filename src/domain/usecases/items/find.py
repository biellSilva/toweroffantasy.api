from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.items import Item
from src.domain.usecases.base import IUsecase


class FindItemsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindItemsUseCase(IUsecase[FindItemsParams, Item], ABC):
    @abstractmethod
    async def execute(self, params: FindItemsParams) -> Item: ...
