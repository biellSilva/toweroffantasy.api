
from pydantic import BaseModel, BeforeValidator
from typing import Annotated


class EntityBase(BaseModel):
    id: Annotated[str, BeforeValidator(lambda x: x.lower())]
    Name: str = 'MISSING'