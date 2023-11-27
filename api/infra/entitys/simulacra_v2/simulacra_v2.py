
from ..simulacra import Simulacra
from ..weapons import Weapon as Weapon_model
from ..matrices import Matrix as Matrix_model


class Simulacra_v2(Simulacra):
    Weapon: Weapon_model | None = None
    Matrix: Matrix_model | None = None

