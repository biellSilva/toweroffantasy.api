from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.researchs import Research
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.researchs.get_all import IGetAllResearchsUseCase
from src.infra.repository.researchs.global_ import ResearchsGlobalRepository


class GetAllResearchsUseCase(IGetAllResearchsUseCase):
    def __init__(self, repository: ResearchsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Research]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
