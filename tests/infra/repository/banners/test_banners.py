import pytest

from src.infra.repository.banners import BannersRepository


class ItemsSuite:

    @pytest.mark.asyncio
    async def global_de_test(self) -> None:
        REPO = BannersRepository()

        DATA = await REPO.get_all()

        assert len(DATA) != 0
