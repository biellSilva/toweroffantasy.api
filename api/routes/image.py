
import aiohttp

from fastapi import APIRouter
from fastapi.responses import Response

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
async def get_asset(path: str, version: VERSIONS = VERSIONS('global')):
    '''
    **Path Param** \n
        path: 
            type: str
            required: True
            desc: Path to asset

    **Query Params** \n
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
                    image = Image.open(BytesIO(data))
                    buffer = BytesIO()
                    image.save(buffer, format='webp', quality=100, optimize=True)
                    buffer.seek(0)
                    return Response(buffer.getvalue(), media_type=f'image/WEBP')
                else:
                    raise AssetNotFound

        elif version == 'china':
            async with cs.get(f'{CN_ASSETS}/{path}') as res:
                if res.status == 200:
                    data = await res.read()
                    image = Image.open(BytesIO(data))
                    buffer = BytesIO()
                    image.save(buffer, format='webp', quality=100, optimize=True)
                    buffer.seek(0)
                    return Response(buffer.getvalue(), media_type=f'image/WEBP')
                else:
                    raise AssetNotFound
        
        else:
            VersionNotFound(version)