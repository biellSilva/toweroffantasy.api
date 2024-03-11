from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.achievements import Achievement

from src.domain.usecases.base import IUsecase


class FindAchievementsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindAchievementsUseCase(IUsecase[FindAchievementsParams, Achievement], ABC):
    @abstractmethod
    async def execute(self, params: FindAchievementsParams) -> Achievement: ...
