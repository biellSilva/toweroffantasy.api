
from src.presentation.controller.gears.find import FindGearsController
from src.main.factories.usecases.gears.find import FindGearsUsecaseFactory

class FindGearsControllerFactory:

    @staticmethod
    def create() -> FindGearsController:
        return FindGearsController(
            FindGearsUsecaseFactory.create()
        )


