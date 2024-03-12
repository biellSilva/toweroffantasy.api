from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from src.domain.models.food import Food
from src.domain.usecases.base import IUsecase


class GetAllFoodParams(BaseModel):
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Game language")
    filter: dict[str, Any] = Field(
        {},
        description="Filter to apply to the models",
        examples=[{"awakening.need": 4000}, {"limited": True}],
    )


class IGetAllFoodUseCase(IUsecase[GetAllFoodParams, Food], ABC):
    @abstractmethod
    async def execute(self, params: GetAllFoodParams) -> list[Food]: ...
