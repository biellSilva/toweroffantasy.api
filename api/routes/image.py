
import aiohttp

from fastapi import APIRouter
from fastapi.responses import Response
from typing import Literal
from PIL import Image
from io import BytesIO

from api.core.exceptions import AssetNotFound, VersionNotFound

from api.enums import VERSIONS
from api.config import GLOBAL_ASSETS, CN_ASSETS


router = APIRouter(prefix='/assets', tags=['Assets'])
METADATA = {
    'name': 'Assets',
    'description': 'Route design to provide Assets/Images \n\n **CONTAINS CN DATA**',
    }


@router.get('/{path:path}')
async def get_asset(path: str, format: Literal['png', 'webp'] = 'png', version: VERSIONS = VERSIONS('global')):
    '''
    **Path Param** \n
        path: 
            type: str
            required: True
            desc: Path to asset

    **Query Params** \n
        format:
            type: string
            default: png
            desc: Choose file format between png or webp, webp is processed before returning
        
        version: 
            type: string
            default: global
            desc: Game version to use
            
    **Return** \n
        Image
    '''

    async with aiohttp.ClientSession() as cs:
        path = path if path.endswith('.png') else f'{path}.png'

        if version == 'global':
            async with cs.get(f'{GLOBAL_ASSETS}/{path}') as res:
                if res.status == 200:
                    data = await res.read()
                    if format == 'webp':
                        image = Image.open(BytesIO(data))
                        buffer = BytesIO()

                        image.save(buffer, format='webp', quality=100, optimize=True)
                        buffer.seek(0)

                        return Response(buffer.getvalue(), media_type=f'image/{format.upper()}')
                    
                    else:
                        return Response(data, media_type=f'image/{format.upper()}')
                    
                else:
                    raise AssetNotFound
                

        elif version == 'china':
            async with cs.get(f'{CN_ASSETS}/{path}') as res:
                if res.status == 200:
                    data = await res.read()
                    if format == 'webp':
                        image = Image.open(BytesIO(data))
                        buffer = BytesIO()

                        image.save(buffer, format='webp', quality=100, optimize=True)
                        buffer.seek(0)

                        return Response(buffer.getvalue(), media_type=f'image/{format.upper()}')
                    
                    else:
                        return Response(data, media_type=f'image/{format.upper()}')
                    
                else:
                    raise AssetNotFound
        
        else:
            VersionNotFound(version)