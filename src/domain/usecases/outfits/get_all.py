from abc import ABC, abstractmethod

from src.domain.models.outfits import Outfit
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllOutfitsUseCase(IUsecase[GetAllParams, Outfit], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Outfit]: ...
