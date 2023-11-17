
from fastapi import APIRouter

from api.enums import OUTFITS, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.repository import MountsRepo
from api.infra.entitys import EntityBase, Mount


router = APIRouter(prefix='/mounts', tags=['Mounts'])

MOUNTS_REPO = MountsRepo()


@router.get('/{id}', name='Get mount', response_model=Mount)
async def get_mount(id: OUTFITS, lang: LANGS = LANGS('en'), include: bool = True):
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
    
    if mount := await MOUNTS_REPO.get(EntityBase(id=id), lang):
        if include:
            return PrettyJsonResponse(mount.model_dump())
        else:
            return PrettyJsonResponse(mount.model_dump(include={'id', 'name', 'assets'}))
    else:
        raise ItemNotFound(detail={'error': f'{id} not found in {lang}'})

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
    
    if mounts := await MOUNTS_REPO.get_all(lang):
        if include:
            return PrettyJsonResponse([mount.model_dump() for mount in mounts])
        else:
            return PrettyJsonResponse([mount.model_dump(include={'name', 'assets'}) for mount in mounts])
    
    else:
        raise ItemNotFound(detail={'error': f'{lang} not found'})