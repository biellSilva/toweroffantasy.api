from src.modules.base.json_repository import JsonRepository
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple


class ImitationRepository(JsonRepository[Simulacrum, SimulacrumSimple]):
    def __init__(self) -> None:
        super().__init__(
            name="simulacra",
            model=Simulacrum,
            simple_model=SimulacrumSimple,
        )
