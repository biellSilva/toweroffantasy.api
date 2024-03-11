from src.data.usecases.outfits.find import FindOutfitsUseCase
from src.infra.repository.outifts.global_ import OutfitsGlobalRepository


class FindOutfitsUsecaseFactory:

    @staticmethod
    def create() -> FindOutfitsUseCase:
        return FindOutfitsUseCase(OutfitsGlobalRepository())
