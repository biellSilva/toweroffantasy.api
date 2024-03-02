from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.weapons import Weapon
from src.domain.usecases.base import IUsecase


class FindWeaponsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindWeaponsUseCase(IUsecase[FindWeaponsParams, Weapon], ABC):
    @abstractmethod
    async def execute(self, params: FindWeaponsParams) -> Weapon: ...
