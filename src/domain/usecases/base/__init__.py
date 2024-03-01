from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel

BMI = TypeVar("BMI", bound=BaseModel)
BMO = TypeVar("BMO", bound=BaseModel)


class IUsecase(ABC, Generic[BMI, BMO]):

    @abstractmethod
    async def execute(self, params: BMI) -> BMO | list[BMO]: ...
