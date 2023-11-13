
from enum import StrEnum
from pathlib import Path
from json import loads


__langs: list[str] = [file.name for file in Path('api/database').iterdir() if file.is_dir()]
LANGS = StrEnum('LANGS', __langs)

__simulacras_names: list[str] = [file for file in loads(Path('api/database/en/imitations.json').read_bytes()) if 'L1' not in file]
SIMULACRAS = StrEnum('SIMULACRAS', __simulacras_names)

__matrices_names: list[str] = [file.replace('_1', '') for file in loads(Path('api/database/en/matrices.json').read_bytes())]
MATRICES = StrEnum('MATRICES', __matrices_names)

__weapons_names: list[str] = [file for file in loads(Path('api/database/en/weapons.json').read_bytes())]
WEAPONS = StrEnum('WEAPONS', __weapons_names)

__relics_names: list[str] = [file for file in loads(Path('api/database/en/relics.json').read_bytes())]
RELICS = StrEnum('RELICS', __relics_names)

__foods_names: list[str] = [file for file in loads(Path('api/database/en/food.json').read_bytes())]
FOOD = StrEnum('FOOD', __foods_names)

__items_names: list[str] = [file for file in loads(Path('api/database/en/items.json').read_bytes())]
ITEMS = StrEnum('ITEMS', __items_names)

__achievs_names: list[str] = [file for file in loads(Path('api/database/en/achievements.json').read_bytes())]
ACHIEVS = StrEnum('ACHIEVS', __achievs_names)

__outfits_names: list[str] = [file for file in loads(Path('api/database/en/outfits.json').read_bytes())]
OUTFITS = StrEnum('OUTFITS', __outfits_names)