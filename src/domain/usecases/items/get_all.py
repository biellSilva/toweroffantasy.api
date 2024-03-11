from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.items import Item

from src.domain.usecases.base import IUsecase


class GetAllItemsParams(BaseModel):
    version: str
    lang: str


class IGetAllItemsUseCase(IUsecase[GetAllItemsParams, Item], ABC):
    @abstractmethod
    async def execute(self, params: GetAllItemsParams) -> list[Item]: ...
