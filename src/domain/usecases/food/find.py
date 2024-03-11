from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.food import Food

from src.domain.usecases.base import IUsecase


class FindFoodParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindFoodUseCase(IUsecase[FindFoodParams, Food], ABC):
    @abstractmethod
    async def execute(self, params: FindFoodParams) -> Food: ...
