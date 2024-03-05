from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.matrices import Matrix
from src.domain.usecases.matrices.get_all import (
    GetAllMatricesParams,
    IGetAllMatricesUseCase,
)
from src.infra.repository.matrices.global_ import MatricesGlobalRepository


class GetAllMatricesUseCase(IGetAllMatricesUseCase):
    def __init__(self, repository: MatricesGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllMatricesParams) -> list[Matrix]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
