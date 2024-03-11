from src.main.factories.usecases.outfits.find import FindOutfitsUsecaseFactory
from src.presentation.controller.outfits.find import FindOutfitsController


class FindOutfitsControllerFactory:

    @staticmethod
    def create() -> FindOutfitsController:
        return FindOutfitsController(FindOutfitsUsecaseFactory.create())
