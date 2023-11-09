
from fastapi.exceptions import HTTPException
from typing import Any, Dict, Optional


class ItemNotFound(HTTPException):
    def __init__(self, status_code: int = 500, detail: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status_code, detail, headers)