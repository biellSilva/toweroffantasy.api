
from src.presentation.controller.gears.get_all import GetAllGearsController
from src.main.factories.usecases.gears.get_all import GetAllGearsUsecaseFactory

class GetAllGearsControllerFactory:

    @staticmethod
    def create() -> GetAllGearsController:
        return GetAllGearsController(
            GetAllGearsUsecaseFactory.create()
        )


