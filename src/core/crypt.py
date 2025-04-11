from datetime import datetime, timedelta
from typing import Any

from bcrypt import checkpw, gensalt, hashpw
from jwt import decode, encode

from src._settings import config
from src._utils import current_datetime


class CryptHelper:
    """Crypt helper.

    This class is responsible for encoding and decoding tokens,
    hashing and checking passwords.
    """

    _AccessToken = str
    _RefreshToken = str

    @classmethod
    def encode(
        cls,
        payload: dict[str, Any],
    ) -> "tuple[ _AccessToken, datetime, _RefreshToken ]":
        """Encode payload."""

        access_expire = current_datetime() + timedelta(seconds=config.ACCESS_EXPIRE)
        # payload["exp"] = access_expire
        access_token = str(encode(payload, key=config.ACCESS_SECRET, algorithm="HS256"))

        # payload["exp"] = current_datetime() + timedelta(seconds=config.REFRESH_EXPIRE)
        refresh_token = str(
            encode(payload, key=config.REFRESH_SECRET, algorithm="HS256"),
        )

        return access_token, access_expire, refresh_token

    @classmethod
    def decode_access(cls, token: _AccessToken) -> dict[str, Any]:
        """Decodes access token."""
        return decode(token, key=config.ACCESS_SECRET, algorithms=["HS256"])

    @classmethod
    def decode_refresh(cls, token: _RefreshToken) -> dict[str, Any]:
        """Decodes refresh token."""
        return decode(token, key=config.REFRESH_SECRET, algorithms=["HS256"])

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
