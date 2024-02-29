from typing import TYPE_CHECKING
from src.infra.models.simulacra import RawSimulacra

if TYPE_CHECKING:
    from src.domain.models.matrices import Matrix
    from src.domain.models.weapons import Weapon


class RawSimulacraV2(RawSimulacra):
    weapon: "Weapon | None"
    matrix: "Matrix | None"
