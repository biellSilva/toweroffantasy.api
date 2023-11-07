from typing import (
    TypeVar,
    Generic,
    Optional
)

from pydantic import BaseModel

B = TypeVar('B', bound=BaseModel)
T = TypeVar('T', bound=BaseModel)


class IRepository(Generic[B, T]):
    __load_all_data__: bool = False
    cache: dict[str, dict[str, T]]

    async def count(self, lang: str) -> int:
        ...

    async def insert(self, model: T, lang: str) -> T:
        ...

    async def get(self, model: B, lang: str) -> Optional[T]:
        ...

    async def get_all(self, lang: str) -> list[T]:
        ...
    
    async def update(self, model: T, lang: str) -> T:
        ...
    
    async def delete(self, model: T, lang: str):
        ...
