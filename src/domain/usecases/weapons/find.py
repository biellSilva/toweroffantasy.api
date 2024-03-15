from abc import ABC, abstractmethod

from src.domain.models.weapons import Weapon
from src.domain.usecases.base import FindParams, IUsecase


class IFindWeaponsUseCase(IUsecase[FindParams, Weapon], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Weapon: ...
