from src.main.factories.usecases.researchs.get_all import GetAllResearchsUsecaseFactory
from src.presentation.controller.researchs.get_all import GetAllResearchsController


class GetAllResearchsControllerFactory:

    @staticmethod
    def create() -> GetAllResearchsController:
        return GetAllResearchsController(GetAllResearchsUsecaseFactory.create())
