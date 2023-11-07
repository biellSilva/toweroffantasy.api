
from pydantic import BaseModel


class EntityBase(BaseModel):
    id: str