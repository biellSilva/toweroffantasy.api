from abc import ABC, abstractmethod
from typing import Any
from fastapi import Query

from pydantic import BaseModel

from src.domain.usecases.base import IUsecase
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class GetallSimulacraParams(BaseModel):
    version: VERSIONS_ENUM = Query(VERSIONS_ENUM("global"), description='Game Version')
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM = Query(LANGS_GLOBAL_ENUM("en"), description='Game language')
    include: bool = Query(False, description='Include all data keys')


class IGetallSimulacraUseCase(IUsecase[GetallSimulacraParams], ABC):
    @abstractmethod
    async def execute(self, params: GetallSimulacraParams) -> list[dict[str, Any]]: ...
