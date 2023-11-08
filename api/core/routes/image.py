
import aiohttp

from fastapi import APIRouter
from fastapi.responses import Response
from typing import Literal

from api.enums import SIMULACRAS

from api.infra.repository import *
from api.infra.entitys import EntityBase
from api.core.exceptions import ItemNotFound


router = APIRouter(prefix='/image', tags=['image'])

SIMU_REPO = SimulacraRepo()


@router.get('/simulacra/{id}')
async def simulacra_image(id: SIMULACRAS, format: Literal['png', 'webp']='webp'):
    if simulacra := await SIMU_REPO.get(EntityBase(id=id), 'en'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://raw.githubusercontent.com/Silyky/Icon_CN/main/UI/huanxing/lihui/{simulacra.avatarID.lower()}.png') as res:
                if res.status == 200:
                    return Response(await res.read(), media_type=f'image/{format.upper()}')
                else:
                    raise ItemNotFound(headers={'error': f'Couldn\'t find {simulacra.id} image'})