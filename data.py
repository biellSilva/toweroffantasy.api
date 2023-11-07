
from api.infra.repository import SimulacraRepo
from api.infra.entitys import EntityBase


SIMU_REPO = SimulacraRepo()

async def foo():
    imits = await SIMU_REPO.get(model=EntityBase(id='imitation_43'), lang='pt')
    print(imits)


import asyncio

asyncio.run(foo())