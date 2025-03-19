from datetime import datetime

from pydantic import BaseModel

from src.modules.users.dtos import UserMe


class LoginParams(BaseModel):
    """Login parameters."""

    email: str
    password: str


class RegisterParams(BaseModel):
    """Register parameters."""

    username: str
    email: str
    password: str


class LoginResponse(BaseModel):
    """Login response."""

    access_token: str
    access_expire: datetime
    refresh_token: str
    user: UserMe


class ChangePasswordParams(BaseModel):
    """Change password parameters."""

    old_password: str
    new_password: str


class Payload(BaseModel):
    """Payload model."""

    id: int
    email: str
    username: str
