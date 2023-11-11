

from api.infra.entitys.simulacra import Simulacra
from api.infra.entitys.weapons import Weapon
from api.infra.entitys.matrices import Matrice


class Simulacra_v2(Simulacra):
    weapon: Weapon | str | None = None    # type: ignore
    matrice: Matrice | None = None

