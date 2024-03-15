from abc import ABC, abstractmethod

from src.domain.models.food import Food
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllFoodUseCase(IUsecase[GetAllParams, Food], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Food]: ...
