import pytest

from src.infra.repository.banners.global_ import BannersGlobalRepository


class BannersSuite:

    @pytest.mark.asyncio
    async def global_banners_test(self) -> None:
        REPO = BannersGlobalRepository()
        DATA = await REPO.get_all()
        assert len(DATA) != 0
