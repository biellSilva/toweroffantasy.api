from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.weapons import Weapon
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.weapons.get_all import IGetAllWeaponsUseCase
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class GetAllWeaponsUseCase(IGetAllWeaponsUseCase):
    def __init__(self, repository: WeaponsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Weapon]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return await filter_models(models, params.filter)
