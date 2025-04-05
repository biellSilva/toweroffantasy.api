from collections.abc import Mapping, Sequence
from typing import Any, Generic, Literal, Self, TypeVar, overload

from src._settings import config
from src.common.base_model import ModelBase
from src.context.mongo_conn import MongoContext

SimpleModel = TypeVar("SimpleModel", bound=ModelBase)
ComplexModel = TypeVar("ComplexModel", bound=ModelBase)


class MongoRepository(Generic[SimpleModel, ComplexModel]):
    """MongoRepository class for MongoDB operations.
    This class is a singleton that provides a connection to the MongoDB database
    and allows for CRUD operations on the specified collection.
    """

    __instance: Self | None = None

    _client = MongoContext.get_client()
    _db = _client.get_database(name=config.MONGO_DB)

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Self:
        """Create a new instance of the MongoRepository class."""
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(
        self,
        collection_name: str,
        simple_model: type[SimpleModel],
        complex_model: type[ComplexModel],
    ) -> None:
        """Initialize the MongoRepository class."""
        self._simple_model = simple_model
        self._complex_model = complex_model

        self._collection_name = collection_name
        self._collection = self._db.get_collection(name=collection_name)

    @overload
    async def get_id(
        self,
        _id: str,
        /,
        *,
        _complex: Literal[True],
    ) -> ComplexModel | None: ...

    @overload
    async def get_id(
        self,
        _id: str,
        /,
        *,
        _complex: Literal[False],
    ) -> SimpleModel | None: ...

    async def get_id(
        self,
        _id: str,
        /,
        *,
        _complex: bool = True,
    ) -> SimpleModel | ComplexModel | None:
        """Get a document by its ID (not ObjectID).

        Args:
            _id (str): The ID of the document to retrieve.
            _complex (bool): Whether to return a complex model or not.

        Returns:
            SimpleModel | ComplexModel | None: The document if found, otherwise None.
        """
        if document := await self._collection.find_one({"id": _id}):
            if _complex:
                return self._complex_model(**document)
            return self._simple_model(**document)
        return None

    @overload
    async def get_object_id(
        self,
        _id: str,
        /,
        *,
        _complex: Literal[True],
    ) -> ComplexModel | None: ...

    @overload
    async def get_object_id(
        self,
        _id: str,
        /,
        *,
        _complex: Literal[False],
    ) -> SimpleModel | None: ...

    async def get_object_id(
        self,
        _id: str,
        /,
        *,
        _complex: bool = False,
    ) -> SimpleModel | ComplexModel | None:
        """Get a document by its ObjectID.

        Args:
            _id (str): The ObjectID of the document to retrieve.
            _complex (bool): Whether to return a complex model or not.
        Returns:
            SimpleModel | ComplexModel | None: The document if found, otherwise None.
        """
        if document := await self._collection.find_one({"_id": _id}):
            if _complex:
                return self._complex_model(**document)
            return self._simple_model(**document)
        return None

    async def get_all(
        self,
        _filter: Mapping[str, Any] | None = None,
        sort: Sequence[tuple[str, str | int | Mapping[str, Any]]] | None = None,
        *,
        skip: int = 0,
        limit: int = 0,
    ) -> list[SimpleModel]:
        """Get all documents in the collection.

        Args:
            _filter (Mapping[str, Any] | None): The filter to apply to the query.
            sort (Sequence[tuple[str, str | int | Mapping[str, Any]]] | None):
            The sort order.
            skip (int): The number of documents to skip.
            limit (int): The maximum number of documents to return.

        Returns:
            list[SimpleModel]: A list of all documents in the collection.
        """
        return [
            self._simple_model(**document)
            async for document in self._collection.find(
                filter=_filter,
                sort=sort,
                skip=skip,
                limit=limit,
            )
        ]

    async def estimated_count(self) -> int:
        """
        Count the number of documents in the collection.
        This method uses the estimated_document_count method to get the count of
        documents in the collection. This method is more efficient than using
        count_documents, but it may not be accurate if documents are being added
        or removed while the count is being performed.

        Args:
            _filter (Mapping[str, Any] | None): The filter to apply to the count.

        Returns:
            int: The number of documents in the collection.
        """
        return await self._collection.estimated_document_count()

    async def count(
        self,
        _filter: Mapping[str, Any] | None = None,
    ) -> int:
        """Count the number of documents in the collection.

        Args:
            _filter (Mapping[str, Any] | None): The filter to apply to the count.

        Returns:
            int: The number of documents in the collection.
        """
        return await self._collection.count_documents(filter=_filter or {})
