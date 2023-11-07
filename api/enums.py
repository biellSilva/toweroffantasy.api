
from enum import StrEnum
from pathlib import Path
from json import loads


__langs: list[str] = [file.name for file in Path('api/database').iterdir() if file.is_dir()]
LANGS = StrEnum('LANGS', __langs)

__simulacras_names: list[str] = [file.name.removesuffix('.json') for file in Path('api/database/en').iterdir() if file.is_file()]
SIMULACRAS = StrEnum('SIMULACRAS', __simulacras_names)

__matrices_names: list[str] = [file for file in loads(Path('api/database/en/matrices.json').read_bytes())]
MATRICES = StrEnum('MATRICES', __matrices_names)

__weapons_names: list[str] = [file.name.removesuffix('.json') for file in Path('api/database/en').iterdir() if file.is_file()]
WEAPONS = StrEnum('WEAPONS', __weapons_names)

__relics_names: list[str] = [file.name.removesuffix('.json') for file in Path('api/database/en').iterdir() if file.is_file()]
RELICS = StrEnum('RELICS', __relics_names)