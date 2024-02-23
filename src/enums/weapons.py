import json
from enum import StrEnum
from pathlib import Path

__weapons_global: list[str] = [
    key.lower()
    for key in dict(
        json.loads(Path("src/infra/database/global/en/weapons.json").read_bytes())
    ).keys()
    if isinstance(key, str)
]
WEAPONS_GLOBAL_ENUM = StrEnum("WEAPONS_GLOBAL_ENUM", __weapons_global)
