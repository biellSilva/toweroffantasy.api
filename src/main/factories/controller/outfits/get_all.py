
from src.presentation.controller.outfits.get_all import GetAllOutfitsController
from src.main.factories.usecases.outfits.get_all import GetAllOutfitsUsecaseFactory

class GetAllOutfitsControllerFactory:

    @staticmethod
    def create() -> GetAllOutfitsController:
        return GetAllOutfitsController(
            GetAllOutfitsUsecaseFactory.create()
        )


