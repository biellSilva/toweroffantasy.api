from src.data.usecases.mount.find import FindMountUseCase
from src.infra.repository.mounts.global_ import MountsGlobalRepository


class FindMountUsecaseFactory:

    @staticmethod
    def create() -> FindMountUseCase:
        return FindMountUseCase(MountsGlobalRepository())
