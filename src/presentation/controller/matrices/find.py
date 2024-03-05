from src.domain.models.matrices import Matrix
from src.domain.usecases.matrices.find import FindMatricesParams, IFindMatricesUseCase


class FindMatricesController:
    def __init__(self, usecase: IFindMatricesUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Matrix:

        return await self.usecase.execute(
            FindMatricesParams(id=id, version=version, lang=lang)
        )
