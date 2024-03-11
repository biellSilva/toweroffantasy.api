from src.main.factories.usecases.gears.find import FindGearsUsecaseFactory
from src.presentation.controller.gears.find import FindGearsController


class FindGearsControllerFactory:

    @staticmethod
    def create() -> FindGearsController:
        return FindGearsController(FindGearsUsecaseFactory.create())
