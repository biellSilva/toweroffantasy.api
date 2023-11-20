
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated


class EntityBase(BaseModel):
    id: Annotated[str, BeforeValidator(lambda x: x.lower())]
    name: str = Field(default=None)