import pytest

from src.enums import LANGS_CHINA_ENUM
from src.infra.repository.matrices.china import MatricesChinaRepository


class MatricesChinaSuite:
    REPO = MatricesChinaRepository()

    @pytest.mark.asyncio
    async def china_cn_test(self) -> None:
        DATA = await self.REPO.get_all(lang=LANGS_CHINA_ENUM("cn"))
        assert len(DATA) != 0
