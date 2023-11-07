
from typing import Optional, TypeVar, Type

from api.infra.interface import IRepository
from api.infra.entitys import EntityBase

B = TypeVar('B', bound=EntityBase)
T = TypeVar('T', bound=EntityBase)


class ModelRepository(IRepository[B, T]):
    def __init__(self, model_base: Type[B], model: Type[T], class_base: Type[IRepository[B, T]], repo_name: str) -> None:
        self.model_base = model_base
        self.model = model
        self.class_base = class_base
        self.repo_name = repo_name
    
    async def get(self, model: B, lang: str) -> Optional[T]:

        if lang in self.class_base.cache:
            if model.id in self.class_base.cache[lang]:
                return self.class_base.cache[lang][model.id]

        else:
            await self.get_all(lang=lang)
            if lang in self.class_base.cache:
                if model.id in self.class_base.cache[lang]:
                    return self.class_base.cache[lang][model.id]