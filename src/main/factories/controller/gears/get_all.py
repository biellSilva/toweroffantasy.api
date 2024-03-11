from src.main.factories.usecases.gears.get_all import GetAllGearsUsecaseFactory
from src.presentation.controller.gears.get_all import GetAllGearsController


class GetAllGearsControllerFactory:

    @staticmethod
    def create() -> GetAllGearsController:
        return GetAllGearsController(GetAllGearsUsecaseFactory.create())
