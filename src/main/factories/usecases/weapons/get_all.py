from src.data.usecases.weapons.get_all import GetAllWeaponsUseCase
from src.infra.repository.weapons.china import WeaponsChinaRepository
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class GetAllWeaponsUsecaseFactory:

    @staticmethod
    def create() -> GetAllWeaponsUseCase:
        return GetAllWeaponsUseCase(WeaponsGlobalRepository(), WeaponsChinaRepository())
