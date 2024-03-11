from src.data.usecases.achievements.find import FindAchievementsUseCase
from src.infra.repository.achievements.global_ import AchievementsGlobalRepository


class FindAchievementsUsecaseFactory:

    @staticmethod
    def create() -> FindAchievementsUseCase:
        return FindAchievementsUseCase(AchievementsGlobalRepository())
