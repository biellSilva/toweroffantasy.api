from src.main.factories.usecases.guidebooks.get_all import (
    GetAllGuidebooksUsecaseFactory,
)
from src.presentation.controller.guidebooks.get_all import GetAllGuidebooksController


class GetAllGuidebooksControllerFactory:

    @staticmethod
    def create() -> GetAllGuidebooksController:
        return GetAllGuidebooksController(GetAllGuidebooksUsecaseFactory.create())
