from typing import Any, Dict

from fastapi import HTTPException, status


class NotFoundErr(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail: Any = "ID not found",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class DataNotFoundErr(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail: Any = "Impossible to reach lang or version data path",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class DataIncompleteErr(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail: Any = (
            "While loading data files something went wrong,"
            " most likely due to a missing file"
        ),
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class NotImplementedErr(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_501_NOT_IMPLEMENTED,
        detail: Any = (
            "Not implemented yet"
        ),
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)
