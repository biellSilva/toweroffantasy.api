import pytest

from src.enums import LANGS_CHINA_ENUM
from src.infra.repository.items.china import ItemsChinaRepository


class ItemsChinaSuite:
    REPO = ItemsChinaRepository()

    @pytest.mark.asyncio
    async def china_cn_test(self) -> None:
        DATA = await self.REPO.get_all(lang=LANGS_CHINA_ENUM("cn"))
        assert len(DATA) != 0
