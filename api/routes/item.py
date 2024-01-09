
from fastapi import APIRouter, Path, Query

from api.enums import ITEMS, LANGS, VERSIONS

from api.infra.entitys import Item, EntityBase
from api.infra.repository import ItemRepo

from api.core.response import PrettyJsonResponse


ITEM_REPO = ItemRepo()

router = APIRouter(prefix="/items", tags=["Items"])
METADATA = {
    'name': 'Items',
    'description': 'Contains most of the items in-game \t\n DOES NOT CONTAINS CN DATA'
}

INCLUDE = {'id', 'name', 'rarity', 'icon'}


@router.get('/{id}', response_model=Item)
async def get_item(id: ITEMS = Path(description='Item ID'), 
                   lang: LANGS = Query(LANGS('en'), description='Language code'), 
                   include: bool = Query(True, description='Include all data keys')):
    '''    
    **Return** \n
        Item
    '''

    item = await ITEM_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(item.model_dump())
    else:
        return PrettyJsonResponse(item.model_dump(include=INCLUDE))
    


@router.get('', response_model=list[Item])
async def get_all_items(lang: LANGS = Query(LANGS('en'), description='Language code'), 
                        include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \n
        List[Item]
    '''

    items = await ITEM_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([item.model_dump() for item in items])
    else:
        return PrettyJsonResponse([item.model_dump(include=INCLUDE) for item in items])