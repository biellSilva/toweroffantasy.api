
import strawberry

from api.infra.entitys.weapons.graphql.weapons import Weapon
from api.infra.entitys.matrices.graphql.matrice import Matrice

from api.infra.entitys.simulacra.graphql.simulacra import Simulacra


@strawberry.type
class SimulacraV2(Simulacra):
    weapon: Weapon | None
    matrice: Matrice | None

