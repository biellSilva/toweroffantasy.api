from abc import ABC, abstractmethod

from src.domain.models.achievements import Achievement
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllAchievementsUseCase(IUsecase[GetAllParams, Achievement], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Achievement]: ...
