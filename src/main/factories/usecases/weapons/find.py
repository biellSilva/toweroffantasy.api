from src.data.usecases.weapons.find import FindWeaponsUseCase
from src.infra.repository.weapons.china import WeaponsChinaRepository
from src.infra.repository.weapons.global_ import WeaponsGlobalRepository


class FindWeaponsUsecaseFactory:

    @staticmethod
    def create() -> FindWeaponsUseCase:
        return FindWeaponsUseCase(WeaponsGlobalRepository(), WeaponsChinaRepository())
