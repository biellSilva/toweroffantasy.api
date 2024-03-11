from src.domain.models.gears import Gear
from src.domain.usecases.gears.find import FindGearsParams, IFindGearsUseCase


class FindGearsController:
    def __init__(self, usecase: IFindGearsUseCase):
        self.usecase = usecase

    async def handle(self, id: str, version: str = "global", lang: str = "en") -> Gear:
        return await self.usecase.execute(
            FindGearsParams(id=id, version=version, lang=lang)
        )
