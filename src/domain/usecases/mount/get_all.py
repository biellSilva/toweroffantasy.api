from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from src.domain.models.mounts import Mount
from src.domain.usecases.base import IUsecase


class GetAllMountParams(BaseModel):
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Game language")
    filter: dict[str, Any] = Field(
        {},
        description="Filter to apply to the models",
        examples=[{"awakening.need": 4000}, {"limited": True}],
    )


class IGetAllMountUseCase(IUsecase[GetAllMountParams, Mount], ABC):
    @abstractmethod
    async def execute(self, params: GetAllMountParams) -> list[Mount]: ...
