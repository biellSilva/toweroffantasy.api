from typing import (
    TypeVar,
    Generic
)

from pydantic import BaseModel

from api.enums import LANGS, LANGS_CN , VERSIONS

B = TypeVar('B', bound=BaseModel)
T = TypeVar('T', bound=BaseModel)


class IRepository(Generic[B, T]):
    __load_all_data__: bool = False
    cache: dict[str, dict[str, dict[str, T]]]

    async def get(self, model: B, lang: LANGS | LANGS_CN, version: VERSIONS) -> T:
        ...

    async def get_by_name(self, name: str, lang: LANGS | LANGS_CN, version: VERSIONS) -> T:
        ...

    async def get_all(self, lang: LANGS | LANGS_CN, version: VERSIONS) -> list[T]:
        ...
    
