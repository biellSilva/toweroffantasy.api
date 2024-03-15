from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.researchs import Research
from src.domain.usecases.base import FindParams
from src.domain.usecases.researchs.find import IFindResearchsUseCase
from src.infra.repository.researchs.global_ import ResearchsGlobalRepository


class FindResearchsUseCase(IFindResearchsUseCase):
    def __init__(self, repository: ResearchsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> Research:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
