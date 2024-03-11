from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.gears import Gear

from src.domain.usecases.base import IUsecase


class FindGearsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindGearsUseCase(IUsecase[FindGearsParams, Gear], ABC):
    @abstractmethod
    async def execute(self, params: FindGearsParams) -> Gear: ...
