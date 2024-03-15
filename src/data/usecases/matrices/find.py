from src.domain.errors.http import NotFoundErr, VersionNotFoundErr
from src.domain.models.matrices import Matrix
from src.domain.usecases.base import FindParams
from src.domain.usecases.matrices.find import IFindMatricesUseCase
from src.infra.repository.matrices.china import MatricesChinaRepository
from src.infra.repository.matrices.global_ import MatricesGlobalRepository


class FindMatricesUseCase(IFindMatricesUseCase):
    def __init__(
        self,
        repository: MatricesGlobalRepository,
        china_repository: MatricesChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: FindParams) -> Matrix:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            if data := await self.china_repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        else:
            raise VersionNotFoundErr
