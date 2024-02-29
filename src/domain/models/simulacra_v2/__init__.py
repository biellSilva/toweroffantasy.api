from src.domain.models.matrices import Matrix
from src.domain.models.simulacra import Simulacra
from src.domain.models.weapons import Weapon


class SimulacraV2(Simulacra):
    weapon: Weapon | None = None
    matrix: Matrix | None = None
