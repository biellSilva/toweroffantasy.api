from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.guidebook import GuideBook
from src.domain.usecases.guidebooks.get_all import (
    GetAllGuidebooksParams,
    IGetAllGuidebooksUseCase,
)
from src.infra.repository.guidebooks.global_ import GuidebooksGlobalRepository


class GetAllGuidebooksUseCase(IGetAllGuidebooksUseCase):
    def __init__(self, repository: GuidebooksGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllGuidebooksParams) -> list[GuideBook]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return filter_models(models, params.filter)
