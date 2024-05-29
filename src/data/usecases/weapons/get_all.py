from src.decorators.filter import filter_models
from src.domain.errors.http import VersionNotFoundErr
from src.domain.models.weapons import Weapon
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.weapons.get_all import IGetAllWeaponsUseCase
from src.infra.repository.weapons.china import WeaponsChinaRepository
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class GetAllWeaponsUseCase(IGetAllWeaponsUseCase):
    def __init__(
        self,
        repository: WeaponsGlobalRepository,
        china_repository: WeaponsChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: GetAllParams) -> list[Weapon]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            models = await self.china_repository.get_all(**params.model_dump())

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
