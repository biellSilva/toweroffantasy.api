
from src.presentation.controller.outfits.find import FindOutfitsController
from src.main.factories.usecases.outfits.find import FindOutfitsUsecaseFactory

class FindOutfitsControllerFactory:

    @staticmethod
    def create() -> FindOutfitsController:
        return FindOutfitsController(
            FindOutfitsUsecaseFactory.create()
        )


