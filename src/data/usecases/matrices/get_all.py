from src.decorators.filter import filter_models
from src.domain.errors.http import VersionNotFoundErr
from src.domain.models.matrices import Matrix
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.matrices.get_all import IGetAllMatricesUseCase
from src.infra.repository.matrices.china import MatricesChinaRepository
from src.infra.repository.matrices.global_ import MatricesGlobalRepository


class GetAllMatricesUseCase(IGetAllMatricesUseCase):
    def __init__(
        self,
        repository: MatricesGlobalRepository,
        china_repository: MatricesChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: GetAllParams) -> list[Matrix]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            models = await self.china_repository.get_all(**params.model_dump())

        else:
            raise VersionNotFoundErr

        return await filter_models(models, params.filter)
