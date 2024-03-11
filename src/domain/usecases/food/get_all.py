from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.food import Food
from src.domain.usecases.base import IUsecase


class GetAllFoodParams(BaseModel):
    version: str
    lang: str


class IGetAllFoodUseCase(IUsecase[GetAllFoodParams, Food], ABC):
    @abstractmethod
    async def execute(self, params: GetAllFoodParams) -> list[Food]: ...
