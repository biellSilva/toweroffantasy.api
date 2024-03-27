import pytest

from src.enums import LANGS_CHINA_ENUM
from src.infra.repository.simulacra_v2.china import SimulacraV2ChinaRepository


class SimualcraChinaSuite:
    REPO = SimulacraV2ChinaRepository()

    @pytest.mark.asyncio
    async def china_cn_test(self) -> None:
        DATA = await self.REPO.get_all(lang=LANGS_CHINA_ENUM("cn"))
        assert len(DATA) != 0
