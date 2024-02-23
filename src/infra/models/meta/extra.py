from typing import TypedDict


class RawLastUpdate(TypedDict):
    username: str
    timestamp: int


class RawRecoMatrice(TypedDict):
    id: str
    pieces: int
