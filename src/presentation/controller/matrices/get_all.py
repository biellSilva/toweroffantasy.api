from src.domain.models.matrices import Matrix
from src.domain.usecases.matrices.get_all import (
    GetAllMatricesParams,
    IGetAllMatricesUseCase,
)


class GetAllMatricesController:
    def __init__(self, usecase: IGetAllMatricesUseCase):
        self.usecase = usecase

    async def handle(self, version: str = "global", lang: str = "en") -> list[Matrix]:
        return await self.usecase.execute(
            GetAllMatricesParams(version=version, lang=lang)
        )
