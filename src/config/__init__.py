from datetime import datetime

from src.utils import current_time

# Last time project restarted
LAST_RESTART: datetime = current_time()


# Project information
PROJECT_NAME: str = "Tower of Fantasy API"
PROJECT_VERSION: str = "2.0.0"
PROJECT_SUMMARY: str = "Made from players to players"
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
PROJECT_LICENSE: dict[str, str] = {"License": "All Rigths Reserved"}
