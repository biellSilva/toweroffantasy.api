
from fastapi import APIRouter, Path, Query

from api.enums import OUTFITS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import OutfitRepo
from api.infra.entitys import EntityBase, Outfit


OUTFIT_REPO = OutfitRepo()

router = APIRouter(prefix='/outfits', tags=['Outfits'])
METADATA = {
    'name': 'Outfits',
    'description': ('Player\'s cloths\t\n'
                    'DOES NOT CONTAINS CN DATA'),
}

INCLUDE = {'id', 'name', 'icon'}


@router.get('/{id}', name='Get outfit', response_model=Outfit)
async def get_outfit(id: OUTFITS = Path(description='Outfit ID'), 
                     lang: LANGS = Query(LANGS('en'), description='Language code'), 
                     include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \n
        Outfit
    '''
    
    outfit = await OUTFIT_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(outfit.model_dump())
    else:
        return PrettyJsonResponse(outfit.model_dump(include={'name', 'icon'}))



@router.get('', name='All outfits', response_model=list[Outfit])
async def get_all_outfits(lang: LANGS = Query(LANGS('en'), description='Language code'), 
                         include: bool = Query(False, description='Include all data keys')):
    '''
    **Return** \n
        List[Outfit]
    '''
    
    outfits = await OUTFIT_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([outfit.model_dump() for outfit in outfits])
    else:
        return PrettyJsonResponse([outfit.model_dump(include={'name', 'icon'}) for outfit in outfits])
    
