
import strawberry

from api.infra.entitys.weapons import Weapon
from api.infra.entitys.matrices import Matrice

from api.infra.entitys.simulacra.graphql.simulacra import SimulacraType


@strawberry.type
class SimulacraTypeV2(SimulacraType):
    weapon: Weapon | None
    matrice: Matrice | None

