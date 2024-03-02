from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.weapons import Weapon
from src.domain.usecases.weapons.get_all import (
    GetAllWeaponsParams,
    IGetAllWeaponsUseCase,
)
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class GetAllWeaponsUseCase(IGetAllWeaponsUseCase):
    def __init__(self, repository: WeaponsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllWeaponsParams) -> list[Weapon]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
