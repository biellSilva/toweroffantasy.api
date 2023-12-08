
from ..simulacra import Simulacra
from ..weapons import Weapon as Weapon_model
from ..matrices import Matrix as Matrix_model


class Simulacra_v2(Simulacra):
    weapon: Weapon_model | None = None
    matrix: Matrix_model | None = None

