
from pydantic import BaseModel, BeforeValidator
from typing import Annotated


class EntityBase(BaseModel):
    id: Annotated[str, BeforeValidator(lambda x: x.lower())]
<<<<<<< Updated upstream
    Name: str = 'MISSING'
=======
    Name: str = Field(default=None)
>>>>>>> Stashed changes
