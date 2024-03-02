import strawberry

from src.domain.models.matrices import Matrix
from src.domain.models.simulacra import Simulacra, SimulacraType
from src.domain.models.weapons import Weapon


class SimulacraV2(Simulacra):
    weapon: Weapon | None = None
    matrix: Matrix | None = None


@strawberry.experimental.pydantic.type(model=SimulacraV2, all_fields=True)
class SimulacraV2Type(SimulacraType):
    pass
