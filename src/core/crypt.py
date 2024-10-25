from datetime import timedelta
from typing import Any

from bcrypt import checkpw, gensalt, hashpw
from jwt import decode, encode

from src._settings import config
from src._utils import current_datetime


class CryptHelper:
    """Crypt helper."""

    @classmethod
    def encode(cls, payload: dict[str, Any], *, stay_logged_in: bool = False) -> str:
        """Encode payload."""
        if stay_logged_in:
            return str(encode(payload, key=config.JWT_SECRET, algorithm="HS256"))

        payload["exp"] = current_datetime() + timedelta(days=1)
        return str(encode(payload, key=config.JWT_SECRET, algorithm="HS256"))

    @classmethod
    def decode(cls, token: str) -> dict[str, Any]:
        """Decode token."""
        return dict(decode(token, key=config.JWT_SECRET, algorithms=["HS256"]))

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Hash password."""
        return hashpw(password.encode(), gensalt()).decode()

    @classmethod
    def check_password(cls, password: str, hashed_password: str) -> bool:
        """Check password."""
        return checkpw(
            password=password.encode(),
            hashed_password=hashed_password.encode(),
        )
