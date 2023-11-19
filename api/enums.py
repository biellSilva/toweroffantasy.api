
from enum import StrEnum
from pathlib import Path
from json import loads


__versions: list[str] = [file.name for file in Path('api/infra/database').iterdir() if file.is_dir()]
VERSIONS = StrEnum('VERSIONS', __versions)


## GLOBAL ENUMS
langs: list[str] = [file.name for file in Path('api/infra/database/global').iterdir() if file.is_dir()]
LANGS = StrEnum('LANGS', langs)

__simulacras_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/imitations.json').read_bytes()) if 'L1' not in file]
SIMULACRA = StrEnum('SIMULACRA', __simulacras_names)

__matrices_names: list[str] = [file.replace('_1', '').lower() for file in loads(Path('api/infra/database/global/en/matrices.json').read_bytes())]
MATRICES = StrEnum('MATRICES', __matrices_names)

__weapons_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/weapons.json').read_bytes())]
WEAPONS = StrEnum('WEAPONS', __weapons_names)

__relics_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/relics.json').read_bytes())]
RELICS = StrEnum('RELICS', __relics_names)

__foods_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/food.json').read_bytes())]
FOOD = StrEnum('FOOD', __foods_names)

__items_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/items.json').read_bytes())]
ITEMS = StrEnum('ITEMS', __items_names)

__achievs_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/achievements.json').read_bytes())]
ACHIEVS = StrEnum('ACHIEVS', __achievs_names)

__outfits_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/outfits.json').read_bytes())]
OUTFITS = StrEnum('OUTFITS', __outfits_names)

__mounts_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/mount.json').read_bytes())]
MOUNTS = StrEnum('MOUNTS', __mounts_names)

__servants_names: list[str] = [file.lower() for file in loads(Path('api/infra/database/global/en/pet.json').read_bytes())]
SERVANTS = StrEnum('SERVANTS', __servants_names)


## CHINA ENUMS
langs_cn: list[str] = [file.name for file in Path('api/infra/database/china').iterdir() if file.is_dir()]
LANGS_CN = StrEnum('LANGS_CN', langs_cn)

__cn_simulacra: list[str] = [file.lower() for file in loads(Path('api/infra/database/china/cn/imitations.json').read_bytes())]
SIMULACRA_CN = StrEnum('CN_SIMULACRA', __cn_simulacra)

__cn_weapons: list[str] = [file.lower() for file in loads(Path('api/infra/database/china/cn/weapons.json').read_bytes())]
WEAPONS_CN = StrEnum('CN_WEAPONS', __cn_weapons)

