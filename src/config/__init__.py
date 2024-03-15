from datetime import datetime
from typing import Any

from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.utils import current_time, project_toml

__PROJECT_TOML = project_toml()


# Last time project restarted
LAST_RESTART: datetime = current_time()


# Project information
PROJECT_NAME: str = __PROJECT_TOML.name
PROJECT_VERSION: str = __PROJECT_TOML.version
PROJECT_SUMMARY: str = __PROJECT_TOML.description
PROJECT_DESC: str = (
    "[Interactive docs](https://api.toweroffantasy.info/docs) \t\n "
    "[Detailed docs](https://api.toweroffantasy.info/redoc) \t\n "
    "[GraphQL docs](https://api.toweroffantasy.info/graphql) \t\n "
    "[Discord](https://discord.com/invite/aida-cafe-670617630717116426) \t\n"
    "[Github](https://github.com/biellSilva/toweroffantasy.api) \t\n "
    "\n"
    "Created by: \t\n "
    "- [biell (API side)](https://github.com/biellSilva) \t\n "
    "- [Emi (ToF Index)](https://github.com/eminentglory) \t\n "
    "- [FortOfFans (Data side)](https://github.com/FortOfFans) \t\n "
    "- [Zakum (ToF Index)](https://github.com/whotookzakum) \t\n "
    "\n"
    "```\t\n"
    f'Last restart: {LAST_RESTART.strftime("%a %d %b %Y, %H:%M:%S %Z%z")}\t\n\n'

    f'Supported versions: {', '.join([value for value in VERSIONS_ENUM])}\t\n\n'

    'Supported languages: \t\n'
    f'Global: {', '.join([value for value in LANGS_GLOBAL_ENUM])}\t\n'
    f'China: {', '.join([value for value in LANGS_CHINA_ENUM])}\t\n'
    '```'
)
PROJECT_LICENSE: dict[str, str] = {"name": __PROJECT_TOML.license.text}


# SWAGGER PARAMS
SWAGGER_UI_PARAMS: dict[str, Any] = {"defaultModelsExpandDepth": -1}  # hide schemas


GLOBAL_ASSETS = "https://raw.githubusercontent.com/FortOfFans/ToF.github.io/main"
GLOBAL_ASSETS_WEBP = "https://raw.githubusercontent.com/FortOfFans/ToF.github.io/webp"

CN_ASSETS = "https://raw.githubusercontent.com/Silyky/Icon_CN/main"
