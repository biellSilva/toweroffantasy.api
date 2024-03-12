from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from src.domain.models.achievements import Achievement
from src.domain.usecases.base import IUsecase


class GetAllAchievementsParams(BaseModel):
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Game language")
    filter: dict[str, Any] = Field(
        {},
        description="Filter to apply to the models",
        examples=[{"awakening.need": 4000}, {"limited": True}],
    )


class IGetAllAchievementsUseCase(IUsecase[GetAllAchievementsParams, Achievement], ABC):
    @abstractmethod
    async def execute(self, params: GetAllAchievementsParams) -> list[Achievement]: ...
