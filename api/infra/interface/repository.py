from typing import (
    TypeVar,
    Generic,
    Optional
)

from pydantic import BaseModel

B = TypeVar('B', bound=str)
T = TypeVar('T', bound=BaseModel)


class IRepository(Generic[B, T]):
    __load_all_data__: bool = False
    cache: dict[str, T]

    async def count(self) -> int:
        ...

    async def insert(self, model: T) -> T:
        ...

    async def get(self, model: B) -> Optional[T]:
        ...

    async def get_all(self) -> list[T]:
        ...
    
    async def update(self, model: T) -> T:
        ...
    
    async def delete(self, model: T):
        ...
