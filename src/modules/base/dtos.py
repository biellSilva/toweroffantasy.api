from datetime import datetime

from pydantic import BaseModel


class BaseDto(BaseModel):
    id: int
    created_at: datetime
