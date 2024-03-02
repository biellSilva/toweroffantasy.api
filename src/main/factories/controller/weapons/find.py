from src.main.factories.usecases.weapons.find import FindWeaponsUsecaseFactory
from src.presentation.controller.weapons.find import FindWeaponsController


class FindWeaponsControllerFactory:

    @staticmethod
    def create() -> FindWeaponsController:
        return FindWeaponsController(FindWeaponsUsecaseFactory.create())
