from src.main.factories.usecases.researchs.find import FindResearchsUsecaseFactory
from src.presentation.controller.researchs.find import FindResearchsController


class FindResearchControllerFactory:

    @staticmethod
    def create() -> FindResearchsController:
        return FindResearchsController(FindResearchsUsecaseFactory.create())
