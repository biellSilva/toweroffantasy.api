from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.matrices import Matrix
from src.domain.usecases.base import FindParams
from src.domain.usecases.matrices.find import IFindMatricesUseCase
from src.infra.repository.matrices.global_ import MatricesGlobalRepository


class FindMatricesUseCase(IFindMatricesUseCase):
    def __init__(self, repository: MatricesGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> Matrix:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
