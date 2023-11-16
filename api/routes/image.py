
import aiohttp

from fastapi import APIRouter
from fastapi.responses import Response, StreamingResponse
from typing import Literal
from PIL import Image
from io import BytesIO

from api.core.exceptions import ItemNotFound


router = APIRouter(prefix='/assets', tags=['assets'])


@router.get('/{path:path}')
async def get_asset(path: str, format: Literal['png', 'webp']='png'):

    async with aiohttp.ClientSession() as cs:
        path = path if '.png' in path else f'{path}.png'

        async with cs.get(f'https://raw.githubusercontent.com/FortOfFans/ToF.github.io/main/{path}') as res:
            if res.status == 200:
                if format == 'webp':
                    image = Image.open(BytesIO(await res.read()))
                    buffer = BytesIO()

                    image.save(buffer, format='webp', quality=100, optimize=True)
                    buffer.seek(0)

                    return StreamingResponse(buffer, media_type=f'image/{format.upper()}')
                
                else:
                    return Response(await res.read(), media_type=f'image/{format.upper()}')
            else:
                raise ItemNotFound(headers={'error': f'Couldn\'t find {path} asset'})