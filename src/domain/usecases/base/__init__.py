from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

BMI = TypeVar("BMI", bound=BaseModel)


class IUsecase(ABC, Generic[BMI]):

    @abstractmethod
    async def execute(self, params: BMI) -> dict[str, Any] | list[dict[str, Any]]: ...
