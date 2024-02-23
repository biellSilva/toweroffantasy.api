from abc import ABC, abstractmethod
from fastapi import Query

from pydantic import BaseModel
from src.domain.models.simulacra import Simulacra

from src.domain.usecases.base import IUsecase
from src.enums import LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class FindSimulacraParams(BaseModel):
    id: str
    version: VERSIONS_ENUM = Query(VERSIONS_ENUM("global"), description="Game version")
    lang: LANGS_GLOBAL_ENUM = Query(
        LANGS_GLOBAL_ENUM("en"), description="Data language"
    )


class FindSimulacraResult(BaseModel):
    result: Simulacra


class IFindSimulacraUseCase(IUsecase[FindSimulacraParams, FindSimulacraResult], ABC):
    @abstractmethod
    async def execute(self, params: FindSimulacraParams) -> FindSimulacraResult: ...
