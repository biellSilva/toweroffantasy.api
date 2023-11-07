
from .simulacra import SimulacraRepo
from .matrice import MatriceRepo
from .weapon import WeaponRepo
from .relics import RelicRepo

__import__ = [
    SimulacraRepo, 
    MatriceRepo, 
    WeaponRepo,
    RelicRepo
]