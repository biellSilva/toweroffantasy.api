from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from src.domain.models.banner import Banner
from src.domain.usecases.base import IUsecase


class FindBannersParams(BaseModel):
    id: str | None = Field(None, description="Banner id")
    version: str = Field("global", description="Game version")
    filter: dict[str, Any] = Field(
        {},
        description="Filter to apply to the models",
        examples=[{"awakening.need": 4000}, {"limited": True}],
    )


class IFindBannersUseCase(IUsecase[FindBannersParams, Banner], ABC):
    @abstractmethod
    async def execute(self, params: FindBannersParams) -> list[Banner]: ...
