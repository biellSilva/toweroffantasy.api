from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.weapons import Weapon
from src.domain.usecases.base import IUsecase


class GetAllWeaponsParams(BaseModel):
    version: str
    lang: str


class IGetAllWeaponsUseCase(IUsecase[GetAllWeaponsParams, Weapon], ABC):
    @abstractmethod
    async def execute(self, params: GetAllWeaponsParams) -> list[Weapon]: ...
