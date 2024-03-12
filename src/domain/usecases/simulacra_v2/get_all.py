from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import IUsecase


class GetAllSimulacraV2Params(BaseModel):
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Game language")
    filter: dict[str, Any] = Field(
        {},
        description="Filter to apply to the models",
        examples=[{"awakening.need": 4000}, {"limited": True}],
    )


class IGetAllSimulacraV2UseCase(IUsecase[GetAllSimulacraV2Params, SimulacraV2], ABC):
    @abstractmethod
    async def execute(self, params: GetAllSimulacraV2Params) -> list[SimulacraV2]: ...
