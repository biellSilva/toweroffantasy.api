
import aiohttp

from fastapi import APIRouter
from fastapi.responses import Response
from typing import Literal

from api.core.exceptions import ItemNotFound


router = APIRouter(prefix='/assets', tags=['assets'])


@router.get('/{path:path}')
async def get_asset(path: str, format: Literal['png', 'webp']='webp'):

    async with aiohttp.ClientSession() as cs:
        path = path if '.png' in path else f'{path}.png'

        async with cs.get(f'https://raw.githubusercontent.com/Silyky/Icon_CN/main/{path}') as res:
            if res.status == 200:
                return Response(await res.read(), media_type=f'image/{format.upper()}')
            else:
                raise ItemNotFound(headers={'error': f'Couldn\'t find {path} asset'})