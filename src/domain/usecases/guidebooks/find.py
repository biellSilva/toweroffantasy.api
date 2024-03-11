from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.guidebook import GuideBook
from src.domain.usecases.base import IUsecase


class FindGuidebooksParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindGuidebooksUseCase(IUsecase[FindGuidebooksParams, GuideBook], ABC):
    @abstractmethod
    async def execute(self, params: FindGuidebooksParams) -> GuideBook: ...
