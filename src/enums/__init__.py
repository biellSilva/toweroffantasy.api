from enum import StrEnum
from pathlib import Path

__versions: list[str] = [folder.name.lower() for folder in Path("").iterdir()]
VERSIONS_ENUM = StrEnum("VERSIONS_ENUM", __versions)


__langs_global: list[str] = [folder.name.lower() for folder in Path("").iterdir()]
LANGS_GLOBAL_ENUM = StrEnum("LANGS_GLOBAL_ENUM", __langs_global)


__langs_china: list[str] = [folder.name.lower() for folder in Path("").iterdir()]
LANGS_CHINA_ENUM = StrEnum("LANGS_CHINA_ENUM", __langs_china)
