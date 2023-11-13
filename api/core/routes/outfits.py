
from fastapi import APIRouter

from api.enums import OUTFITS, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.repository import OutfitRepo
from api.infra.entitys import EntityBase, Outfit


router = APIRouter(prefix='/outfit', tags=['outfit'])

OUTFIT_REPO = OutfitRepo()


@router.get('/{id}', name='Get outfit', response_model=Outfit)
async def get_outfit(id: OUTFITS, lang: LANGS = LANGS('en')):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: outfit_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        Outfit
    '''
    
    if outfit := await OUTFIT_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(outfit.model_dump())

    else:
        raise ItemNotFound(detail={'error': f'{id} not found in {lang}'})

@router.get('', name='All outfits', response_model=list[Outfit])
async def get_all_outfits(lang: LANGS = LANGS('en')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        List[Outfit]
    '''
    
    if outfits := await OUTFIT_REPO.get_all(lang):
        return PrettyJsonResponse([outfit.model_dump() for outfit in outfits])
    
    else:
        raise ItemNotFound(detail={'error': f'{lang} not found'})