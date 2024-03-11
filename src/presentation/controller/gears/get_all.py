from src.domain.models.gears import Gear
from src.domain.usecases.gears.get_all import GetAllGearsParams, IGetAllGearsUseCase


class GetAllGearsController:
    def __init__(self, usecase: IGetAllGearsUseCase):
        self.usecase = usecase

    async def handle(self, version: str = "global", lang: str = "en") -> list[Gear]:
        return await self.usecase.execute(GetAllGearsParams(version=version, lang=lang))
