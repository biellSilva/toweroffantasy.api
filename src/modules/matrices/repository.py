from typing import TYPE_CHECKING, Any

from src.common.mongo_repository import MongoRepository
from src.modules.matrices.model import Suit

if TYPE_CHECKING:
    from src.modules.matrices.dtos import GetMatrices, GetMatrix


class MatriceRepository(MongoRepository[Suit, Suit]):
    def __init__(self) -> None:
        super().__init__(
            collection_name="matrices",
            simple_model=Suit,
            complex_model=Suit,
        )
        self.view = self._db.get_collection("MatricesView")

    async def get_matrices(self, params: "GetMatrices") -> list[Suit]:
        """Get all matrices."""
        return [
            self._simple_model.model_validate(document, context={"lang": params.lang})
            async for document in self.view.find(
                self._filter(params),
                sort=[
                    ("position", -1),
                    ("quality", -1),
                ],
            )
        ]

    async def get_matrix(self, params: "GetMatrix") -> Suit | None:
        """Get a matrix by its ID."""
        if document := await self.view.find_one(
            {"id": {"$regex": params.matrix_id, "$options": "i"}},
        ):
            return self._complex_model.model_validate(
                document,
                context={"lang": params.lang},
            )
        return None

    async def count_matrices(self, params: "GetMatrices") -> int:
        """Count matrices based on the given parameters."""
        return await self.view.count_documents(self._filter(params))

    def _filter(self, params: "GetMatrices") -> dict[str, Any]:
        """Filter matrices based on the given parameters."""
        query: dict[str, Any] = {}

        if params.include_ids:
            query["id"] = {"$in": params.include_ids}
        if params.exclude_ids:
            if "include_ids" in query:
                query["id"]["$nin"] = params.exclude_ids
            else:
                query["id"] = {"$nin": params.exclude_ids}

        return query
