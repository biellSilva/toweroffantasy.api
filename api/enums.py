from enum import StrEnum
from json import loads
from pathlib import Path

__versions: list[str] = [
    file.name for file in Path("api/infra/database").iterdir() if file.is_dir()
]
VERSIONS = StrEnum("VERSIONS", __versions)

__levels: list[str] = [str(i) for i in range(1, 21)]
LEVELS = StrEnum("LEVELS", __levels)


## GLOBAL ENUMS
langs: list[str] = [
    file.name for file in Path("api/infra/database/global").iterdir() if file.is_dir()
]
LANGS = StrEnum("LANGS", langs)

__global_simulacra: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/imitations.json").read_bytes())
    if "L1" not in file
]
SIMULACRA = StrEnum("SIMULACRA", __global_simulacra)

__global_matrices: list[str] = [
    str(file).replace("_1", "").lower()
    for file in loads(Path("api/infra/database/global/en/matrices.json").read_bytes())
]
MATRICES = StrEnum("MATRICES", __global_matrices)

__global_weapons: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/weapons.json").read_bytes())
]
WEAPONS = StrEnum("WEAPONS", __global_weapons)

__global_relics: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/relics.json").read_bytes())
]
RELICS = StrEnum("RELICS", __global_relics)

__global_food: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/food.json").read_bytes())
]
FOOD = StrEnum("FOOD", __global_food)

__global_items: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/items.json").read_bytes())
]
ITEMS = StrEnum("ITEMS", __global_items)

__global_achievs: list[str] = [
    str(file).lower()
    for file in loads(
        Path("api/infra/database/global/en/achievements.json").read_bytes()
    )
]
ACHIEVS = StrEnum("ACHIEVS", __global_achievs)

__global_outfits: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/outfits.json").read_bytes())
]
OUTFITS = StrEnum("OUTFITS", __global_outfits)

__global_mounts: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/mount.json").read_bytes())
]
MOUNTS = StrEnum("MOUNTS", __global_mounts)

__global_servants: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/pet.json").read_bytes())
]
SERVANTS = StrEnum("SERVANTS", __global_servants)

__global_guidbooks: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/global/en/guidebook.json").read_bytes())
]
GUIDEBOOKS = StrEnum("GUIDEBOOKS", __global_guidbooks)

## CHINA ENUMS
langs_cn: list[str] = [
    file.name for file in Path("api/infra/database/china").iterdir() if file.is_dir()
]
LANGS_CN = StrEnum("LANGS_CN", langs_cn)

__cn_simulacra: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/china/cn/imitations.json").read_bytes())
]
SIMULACRA_CN = StrEnum("SIMULACRA_CN", __cn_simulacra)

__cn_weapons: list[str] = [
    str(file).lower()
    for file in loads(Path("api/infra/database/china/cn/weapons.json").read_bytes())
]
WEAPONS_CN = StrEnum("WEAPONS_CN", __cn_weapons)
