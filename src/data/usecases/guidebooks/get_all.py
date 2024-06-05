from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.guidebook import GuideBook
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.guidebooks.get_all import IGetAllGuidebooksUseCase
from src.infra.repository.guidebooks.global_ import GuidebooksGlobalRepository


class GetAllGuidebooksUseCase(IGetAllGuidebooksUseCase):
    def __init__(self, repository: GuidebooksGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[GuideBook]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
