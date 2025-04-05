from typing import TYPE_CHECKING

from src.common.mongo_repository import MongoRepository
from src.modules.simulacra._utils import filter_simulacra
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple

if TYPE_CHECKING:
    from src.modules.simulacra.dtos import GetSimulacra, GetSimulacrum


class SimulacraRepository(MongoRepository[SimulacrumSimple, Simulacrum]):
    """Repository for Simulacra."""

    def __init__(self) -> None:
        super().__init__(
            collection_name="simulacra",
            simple_model=SimulacrumSimple,
            complex_model=Simulacrum,
        )
        self.view = self._db.get_collection("SimulacraView")

    async def get_simulacrum(self, params: "GetSimulacrum") -> Simulacrum | None:
        """Get a Simulacrum by ID."""
        if data := await self.view.find_one(filter={"id": params.simulacrum_id}):
            return self._complex_model.model_validate(
                data,
                context={"lang": params.lang},
            )
        return None

    async def get_simulacra(self, params: "GetSimulacra") -> list[SimulacrumSimple]:
        """Get all Simulacra."""
        return [
            self._simple_model(**document)
            if not params.lang
            else self._simple_model.model_validate(
                document,
                context={"lang": params.lang},
            )
            async for document in self.view.find(
                filter=filter_simulacra(params),
                skip=(params.page - 1) * params.limit,
                limit=params.limit,
                sort=[
                    ("position", -1),
                    ("is_limited", -1),
                    ("no_weapon", -1),
                    ("rarity", -1),
                ],
            )
        ]

    async def count_simulacra(self, params: "GetSimulacra") -> int:
        """Count all Simulacra."""
        return await super().count(filter_simulacra(params))
