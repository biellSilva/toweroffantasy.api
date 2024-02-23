import json
from enum import StrEnum
from pathlib import Path

__simulacras_global: list[str] = [
    key.lower()
    for key in dict(json.loads(Path("").read_bytes())).keys()
    if isinstance(key, str)
]
SIMULACRAS_GLOBAL_ENUM = StrEnum("SIMULACRAS_GLOBAL_ENUM", __simulacras_global)
