
from fastapi import APIRouter, Path, Query

from api.enums import MOUNTS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import MountsRepo
from api.infra.entitys import EntityBase, Mount


MOUNTS_REPO = MountsRepo()

router = APIRouter(prefix='/mounts', tags=['Mounts'])
METADATA = {
    'name': 'Mounts',
    'description': 'Mounts are "vehicles" so the player can move faster around the map \t\n'
    'DOES NOT CONTAINS CN DATA',
}

INCLUDE = {'id', 'name', 'assets'}


@router.get('/{id}', name='Get mount', response_model=Mount)
async def get_mount(id: MOUNTS = Path(description='Mount ID'), 
                    lang: LANGS = Query(LANGS('en'), description='Language code'), 
                    include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \n
        Mount
    '''
    
    mount = await MOUNTS_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(mount.model_dump())
    else:
        return PrettyJsonResponse(mount.model_dump(include=INCLUDE))


@router.get('', name='All mounts', response_model=list[Mount])
async def get_all_mounts(lang: LANGS = Query(LANGS('en'), description='Language code'), 
                         include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \n
        List[Mount]
    '''
    
    mounts = await MOUNTS_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([mount.model_dump() for mount in mounts])
    else:
        return PrettyJsonResponse([mount.model_dump(include=INCLUDE) for mount in mounts])
    