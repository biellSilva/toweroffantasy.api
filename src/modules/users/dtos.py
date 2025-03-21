from datetime import datetime

from prisma.enums import Roles
from pydantic import BaseModel


class UpdateUser(BaseModel):
    """Data Transfer Object for updating a user."""

    username: str | None = None


class User(BaseModel):
    """Data Transfer Object for exporting a user."""

    id: int
    created_at: datetime
    username: str


class UserMe(User):
    """Data Transfer Object for exporting a user."""

    email: str
    roles: list[Roles]
