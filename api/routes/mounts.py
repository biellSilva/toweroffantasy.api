
from fastapi import APIRouter

from api.enums import MOUNTS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import MountsRepo
from api.infra.entitys import EntityBase, Mount


MOUNTS_REPO = MountsRepo()

router = APIRouter(prefix='/mounts', tags=['Mounts'])
METADATA = {
    'name': 'Mounts',
    'description': 'Mounts are "vehicles" so the player can move faster around the map \n\n **DOES NOT CONTAINS CN DATA**',
    }


@router.get('/{id}', name='Get mount', response_model=Mount)
async def get_mount(id: MOUNTS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: mount_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: True
            desc: Include all data keys
            
    **Return** \n
        Mount
    '''
    
    mount = await MOUNTS_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(mount.model_dump())
    else:
        return PrettyJsonResponse(mount.model_dump(include={'id', 'name', 'assets'}))


@router.get('', name='All mounts', response_model=list[Mount])
async def get_all_mounts(lang: LANGS = LANGS('en'), include: bool = False):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use

        include:
            type: bool
            default: False
            desc: Include all data keys
            
    **Return** \n
        List[Mount]
    '''
    
    mounts = await MOUNTS_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([mount.model_dump() for mount in mounts])
    else:
        return PrettyJsonResponse([mount.model_dump(include={'name', 'assets'}) for mount in mounts])
    