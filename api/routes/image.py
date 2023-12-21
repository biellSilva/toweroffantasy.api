
import aiohttp

from fastapi import APIRouter
from fastapi.responses import Response, RedirectResponse

from PIL import Image
from io import BytesIO

from api.core.exceptions import AssetNotFound, VersionNotFound

from api.enums import VERSIONS
from api.config import CN_ASSETS, GLOBAL_ASSETS_WEBP


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

    if version == 'global':
        path = path if path.endswith('.webp') else f'{path}.webp'
        return RedirectResponse(url=f'{GLOBAL_ASSETS_WEBP}/{path}')

    elif version == 'china':
        path = path if path.endswith('.png') else f'{path}.png'
        async with aiohttp.ClientSession() as cs:
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