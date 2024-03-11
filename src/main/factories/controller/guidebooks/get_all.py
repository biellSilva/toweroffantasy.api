
from src.presentation.controller.guidebooks.get_all import GetAllGuidebooksController
from src.main.factories.usecases.guidebooks.get_all import GetAllGuidebooksUsecaseFactory

class GetAllGuidebooksControllerFactory:

    @staticmethod
    def create() -> GetAllGuidebooksController:
        return GetAllGuidebooksController(
            GetAllGuidebooksUsecaseFactory.create()
        )


