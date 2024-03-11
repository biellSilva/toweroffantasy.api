from src.data.usecases.outfits.get_all import GetAllOutfitsUseCase
from src.infra.repository.outifts.global_ import OutfitsGlobalRepository


class GetAllOutfitsUsecaseFactory:

    @staticmethod
    def create() -> GetAllOutfitsUseCase:
        return GetAllOutfitsUseCase(OutfitsGlobalRepository())
