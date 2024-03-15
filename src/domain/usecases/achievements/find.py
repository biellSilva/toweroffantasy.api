from abc import ABC, abstractmethod

from src.domain.models.achievements import Achievement
from src.domain.usecases.base import FindParams, IUsecase


class IFindAchievementsUseCase(IUsecase[FindParams, Achievement], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Achievement: ...
