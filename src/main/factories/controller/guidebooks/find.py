from src.main.factories.usecases.guidebooks.find import FindGuidebooksUsecaseFactory
from src.presentation.controller.guidebooks.find import FindGuidebooksController


class FindGuidebooksControllerFactory:

    @staticmethod
    def create() -> FindGuidebooksController:
        return FindGuidebooksController(FindGuidebooksUsecaseFactory.create())
