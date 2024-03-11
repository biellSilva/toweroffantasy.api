from src.data.usecases.banners.find import FindBannersUseCase
from src.infra.repository.banners.global_ import BannersGlobalRepository


class FindBannersUsecaseFactory:

    @staticmethod
    def create() -> FindBannersUseCase:
        return FindBannersUseCase(BannersGlobalRepository())
