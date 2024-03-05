from src.data.usecases.mount.get_all import GetAllMountUseCase
from src.infra.repository.mounts.global_ import MountsGlobalRepository


class GetAllMountUsecaseFactory:

    @staticmethod
    def create() -> GetAllMountUseCase:
        return GetAllMountUseCase(MountsGlobalRepository())
