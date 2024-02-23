from abc import ABC, abstractmethod
from typing import Optional

from src.domain.models.simulacra import Simulacra
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class FindSimulacraRepository(ABC):
    @abstractmethod
    async def find_by_id(
        self,
        id: str,
        version: VERSIONS_ENUM,
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    ) -> Optional[Simulacra]: ...
