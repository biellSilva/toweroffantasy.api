from abc import ABC, abstractmethod

from pydantic import BaseModel, Field
from src.domain.models.simulacra import Simulacra

from src.domain.usecases.base import IUsecase


class FindSimulacraParams(BaseModel):
    id: str = Field(description="Simulacrum ID")
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Data language")


class IFindSimulacraUseCase(IUsecase[FindSimulacraParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: FindSimulacraParams) -> Simulacra: ...
