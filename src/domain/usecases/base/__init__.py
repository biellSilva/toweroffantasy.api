from abc import ABC, abstractmethod
from typing import Annotated, Generic, TypeVar

from fastapi import Path, Query
from pydantic import BaseModel


class FindParams(BaseModel):
    id: Annotated[
        str,
        Path(
            title="Object ID",
            description="ID of the object to be found",
            example="imitation_30",
        ),
    ]
    version: Annotated[
        str,
        Query(
            default="global",
            title="Game version",
            description="Game version to look for the object in",
            examples=["global", "china"],
        ),
    ]
    lang: Annotated[
        str,
        Query(
            default="en",
            title="In-game language",
            description="Language to look for the object in",
            examples=["en", "ja", "es"],
        ),
    ]


class GetAllParams(BaseModel):
    version: Annotated[
        str,
        Query(
            default="global",
            title="Game version",
            description="Game version to look for the object in",
            examples=["global", "china"],
        ),
    ]
    lang: Annotated[
        str,
        Query(
            default="en",
            title="In-game language",
            description="Language to look for the object in",
            examples=["en", "ja", "es"],
        ),
    ]
    filter: Annotated[
        str | None,
        Query(
            default=None,
            title="Object filter",
            description="Json object in string format like mongodb filter function",
            examples=['{"element": "Flame"}', '{"voiceActors.en": "Keanu Reeves"}'],
        ),
    ]
    limit: int | None = None


BMI = TypeVar("BMI", bound=BaseModel)
BMO = TypeVar("BMO", bound=BaseModel)


class IUsecase(ABC, Generic[BMI, BMO]):

    @abstractmethod
    async def execute(self, params: BMI) -> BMO | list[BMO]: ...
