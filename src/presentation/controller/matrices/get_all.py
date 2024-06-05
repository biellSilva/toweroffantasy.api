from src.domain.models.matrices import Matrix
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.matrices.get_all import IGetAllMatricesUseCase


class GetAllMatricesController:
    def __init__(self, usecase: IGetAllMatricesUseCase):
        self.usecase = usecase

    async def handle(
        self,
        version: str = "global",
        lang: str = "en",
        filter: str | None = None,
        limit: int | None = None,
    ) -> list[Matrix]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter, limit=limit)
        )
