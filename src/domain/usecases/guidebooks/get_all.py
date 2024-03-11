
from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.guidebook import GuideBook

from src.domain.usecases.base import IUsecase


class GetAllGuidebooksParams(BaseModel):
    version: str
    lang: str



class IGetAllGuidebooksUseCase(IUsecase[GetAllGuidebooksParams, GuideBook], ABC):
    @abstractmethod
    async def execute(self, params: GetAllGuidebooksParams) -> list[GuideBook]: ...


