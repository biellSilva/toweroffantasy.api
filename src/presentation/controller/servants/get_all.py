from src.domain.models.servants import SmartServant
from src.domain.usecases.servants.get_all import (
    GetAllServantsParams,
    IGetAllServantsUseCase,
)


class GetAllServantsController:
    def __init__(self, usecase: IGetAllServantsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en"
    ) -> list[SmartServant]:
        return await self.usecase.execute(
            GetAllServantsParams(version=version, lang=lang)
        )
