from abc import ABC, abstractmethod
from fastapi import Path, Query

from pydantic import BaseModel
from src.domain.models.simulacra import Simulacra

from src.domain.usecases.base import IUsecase
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class FindSimulacraParams(BaseModel):
    id: str = Path(description="Simulacrum ID")
    version: VERSIONS_ENUM = Query(VERSIONS_ENUM("global"), description="Game version")
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM = Query(
        LANGS_GLOBAL_ENUM("en"), description="Data language"
    )


class IFindSimulacraUseCase(IUsecase[FindSimulacraParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: FindSimulacraParams) -> Simulacra: ...
