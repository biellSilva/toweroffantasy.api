from src.main.factories.usecases.outfits.get_all import GetAllOutfitsUsecaseFactory
from src.presentation.controller.outfits.get_all import GetAllOutfitsController


class GetAllOutfitsControllerFactory:

    @staticmethod
    def create() -> GetAllOutfitsController:
        return GetAllOutfitsController(GetAllOutfitsUsecaseFactory.create())
