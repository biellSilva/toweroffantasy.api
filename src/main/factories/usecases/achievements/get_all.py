from src.data.usecases.achievements.get_all import GetAllAchievementsUseCase
from src.infra.repository.achievements.global_ import AchievementsGlobalRepository


class GetAllAchievementsUsecaseFactory:

    @staticmethod
    def create() -> GetAllAchievementsUseCase:
        return GetAllAchievementsUseCase(AchievementsGlobalRepository())
