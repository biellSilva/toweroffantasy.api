from datetime import datetime

from pydantic import BaseModel


class UpdateUser(BaseModel):
    """Data Transfer Object for updating a user."""

    username: str | None = None


class User(BaseModel):
    """Data Transfer Object for exporting a user."""

    id: int
    created_at: datetime
    username: str
    email: str
