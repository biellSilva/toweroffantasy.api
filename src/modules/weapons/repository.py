from src.modules.base.cache import RedisCache
from src.modules.base.json_repository import JsonRepository


class WeaponRepository(JsonRepository):
    def __init__(self) -> None:
        self._cache = RedisCache(name="weapons")
