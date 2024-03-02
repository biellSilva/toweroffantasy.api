from src.main.factories.usecases.weapons.get_all import GetAllWeaponsUsecaseFactory
from src.presentation.controller.weapons.get_all import GetAllWeaponsController


class GetAllWeaponsControllerFactory:

    @staticmethod
    def create() -> GetAllWeaponsController:
        return GetAllWeaponsController(GetAllWeaponsUsecaseFactory.create())
