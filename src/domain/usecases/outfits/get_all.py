from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.outfits import Outfit
from src.domain.usecases.base import IUsecase


class GetAllOutfitsParams(BaseModel):
    version: str
    lang: str


class IGetAllOutfitsUseCase(IUsecase[GetAllOutfitsParams, Outfit], ABC):
    @abstractmethod
    async def execute(self, params: GetAllOutfitsParams) -> list[Outfit]: ...
