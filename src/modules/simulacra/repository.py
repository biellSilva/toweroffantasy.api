from src.common.json_repository import JsonRepository
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple


class ImitationRepository(JsonRepository[SimulacrumSimple, Simulacrum]):
    def __init__(self) -> None:
        super().__init__(
            filename="simulacra",
            simple_model=SimulacrumSimple,
            model=Simulacrum,
        )
