from abc import ABC, abstractmethod


from src.domain.models.outfits import Outfit
from src.domain.usecases.base import FindParams, IUsecase


class IFindOutfitsUseCase(IUsecase[FindParams, Outfit], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Outfit: ...
