from datetime import datetime
from typing import Any

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
    f'Last restart: {LAST_RESTART.strftime("%a %d %b %Y, %H:%M:%S %Z%z")}'
)
PROJECT_LICENSE: dict[str, str] = {"name": __PROJECT_TOML.license.text}


# SWAGGER PARAMS
SWAGGER_UI_PARAMS: dict[str, Any] = {"defaultModelsExpandDepth": -1}  # hide schemas