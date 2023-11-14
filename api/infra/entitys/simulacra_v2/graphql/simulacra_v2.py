
import strawberry

from api.infra.entitys.weapons.graphql.weapons import WeaponType
from api.infra.entitys.matrices.graphql.matrice import MatriceType

from api.infra.entitys.simulacra.graphql.simulacra import SimulacraType


@strawberry.type
class SimulacraTypeV2(SimulacraType):
    weapon: WeaponType | None
    matrice: MatriceType | None

