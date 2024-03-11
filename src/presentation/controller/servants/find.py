from src.domain.models.servants import SmartServant
from src.domain.usecases.servants.find import FindServantsParams, IFindServantsUseCase


class FindServantsController:
    def __init__(self, usecase: IFindServantsUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> SmartServant:
        return await self.usecase.execute(
            FindServantsParams(id=id, version=version, lang=lang)
        )
