from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.simulacra import Simulacra

from src.domain.usecases.base import IUsecase
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class GetallSimulacraParams(BaseModel):
    version: VERSIONS_ENUM = VERSIONS_ENUM("global")
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM = LANGS_GLOBAL_ENUM("en")


class IGetallSimulacraUseCase(IUsecase[GetallSimulacraParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: GetallSimulacraParams) -> list[Simulacra]: ...
