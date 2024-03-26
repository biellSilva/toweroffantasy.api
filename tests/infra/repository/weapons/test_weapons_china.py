import pytest

from src.enums import LANGS_CHINA_ENUM
from src.infra.repository.weapons.china import WeaponsChinaRepository


class WeaponsChinaSuite:
    REPO = WeaponsChinaRepository()

    @pytest.mark.asyncio
    async def china_cn_test(self) -> None:
        DATA = await self.REPO.get_all(lang=LANGS_CHINA_ENUM("cn"))
        assert len(DATA) != 0
