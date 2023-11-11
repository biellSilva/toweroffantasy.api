
from pydantic import BaseModel


class Award(BaseModel):
    type: str
    amount: int