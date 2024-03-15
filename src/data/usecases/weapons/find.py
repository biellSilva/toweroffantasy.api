from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.weapons import Weapon
from src.domain.usecases.base import FindParams
from src.domain.usecases.weapons.find import IFindWeaponsUseCase
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class FindWeaponsUseCase(IFindWeaponsUseCase):
    def __init__(self, repository: WeaponsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> Weapon:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
