from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import IUsecase


class GetallSimulacraParams(BaseModel):
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Game language")


class IGetallSimulacraUseCase(IUsecase[GetallSimulacraParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: GetallSimulacraParams) -> list[Simulacra]: ...
