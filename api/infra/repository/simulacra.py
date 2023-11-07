
from api.infra.interface import IRepository
from api.infra.entitys import Simulacra


class SimulacraRepo(IRepository[str, Simulacra]):
    cache: dict[str, Simulacra]
    def __init__(self) -> None:
        super().__init__()  