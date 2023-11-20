
from pydantic import BaseModel


class ExceptionModel(BaseModel):
    status: int
    detail: str | None