
from src.presentation.controller.relics.find import FindRelicsController
from src.main.factories.usecases.relics.find import FindRelicsUsecaseFactory

class FindRelicsControllerFactory:

    @staticmethod
    def create() -> FindRelicsController:
        return FindRelicsController(
            FindRelicsUsecaseFactory.create()
        )


