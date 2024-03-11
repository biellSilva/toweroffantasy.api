
from src.presentation.controller.guidebooks.find import FindGuidebooksController
from src.main.factories.usecases.guidebooks.find import FindGuidebooksUsecaseFactory

class FindGuidebooksControllerFactory:

    @staticmethod
    def create() -> FindGuidebooksController:
        return FindGuidebooksController(
            FindGuidebooksUsecaseFactory.create()
        )


