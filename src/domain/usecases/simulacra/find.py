from abc import ABC, abstractmethod
from typing import Any

from fastapi import Path, Query
from pydantic import BaseModel

from src.domain.usecases.base import IUsecase
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class FindSimulacraParams(BaseModel):
    id: str = Path(description="Simulacrum ID")
    version: VERSIONS_ENUM = Query(VERSIONS_ENUM("global"), description="Game version")
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM = Query(
        LANGS_GLOBAL_ENUM("en"), description="Data language"
    )
    include: bool = Query(default=True, description="Include all keys")


class IFindSimulacraUseCase(IUsecase[FindSimulacraParams], ABC):
    @abstractmethod
    async def execute(self, params: FindSimulacraParams) -> dict[str, Any]: ...
