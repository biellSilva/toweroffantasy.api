from abc import ABC, abstractmethod

from src.domain.models.food import Food
from src.domain.usecases.base import FindParams, IUsecase


class IFindFoodUseCase(IUsecase[FindParams, Food], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Food: ...
