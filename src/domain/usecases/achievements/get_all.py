from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.achievements import Achievement
from src.domain.usecases.base import IUsecase


class GetAllAchievementsParams(BaseModel):
    version: str
    lang: str


class IGetAllAchievementsUseCase(IUsecase[GetAllAchievementsParams, Achievement], ABC):
    @abstractmethod
    async def execute(self, params: GetAllAchievementsParams) -> list[Achievement]: ...
