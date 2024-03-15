import json

from src.domain.models.gears import Gear
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.gears.get_all import IGetAllGearsUseCase


class GetAllGearsController:
    def __init__(self, usecase: IGetAllGearsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Gear]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
