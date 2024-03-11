from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.outfits import Outfit

from src.domain.usecases.base import IUsecase


class FindOutfitsParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindOutfitsUseCase(IUsecase[FindOutfitsParams, Outfit], ABC):
    @abstractmethod
    async def execute(self, params: FindOutfitsParams) -> Outfit: ...
