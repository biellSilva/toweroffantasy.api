from src.domain.errors.http import NotFoundErr, VersionNotFoundErr
from src.domain.models.weapons import Weapon
from src.domain.usecases.base import FindParams
from src.domain.usecases.weapons.find import IFindWeaponsUseCase
from src.infra.repository.weapons.china import WeaponsChinaRepository
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class FindWeaponsUseCase(IFindWeaponsUseCase):
    def __init__(
        self,
        repository: WeaponsGlobalRepository,
        china_repository: WeaponsChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: FindParams) -> Weapon:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            if data := await self.china_repository.find_by_id(**params.model_dump()):
                return data

            raise NotFoundErr

        else:
            raise VersionNotFoundErr
