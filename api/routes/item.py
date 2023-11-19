
from fastapi import APIRouter

from api.enums import ITEMS, LANGS, VERSIONS

from api.infra.entitys import Item, EntityBase
from api.infra.repository import ItemRepo

from api.core.response import PrettyJsonResponse


ITEM_REPO = ItemRepo()

router = APIRouter(prefix="/items", tags=["Items"])
METADATA = {
    'name': 'Items',
    'description': 'Contains most of the items in-game \n\n **DOES NOT CONTAINS CN DATA**'
    }


@router.get('/{id}', response_model=Item)
async def get_item(id: ITEMS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: item_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: True
            desc: Include all data keys
            
    return \n
        Item
    '''

    item = await ITEM_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(item.model_dump())
    else:
        return PrettyJsonResponse(item.model_dump(include={'id', 'name', 'rarity', 'icon'}))
    


@router.get('', response_model=list[Item])
async def get_all_items(lang: LANGS = LANGS('en'), include: bool = False):
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
            
    return \n
        List[Item]
    '''

    items = await ITEM_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([item.model_dump() for item in items])
    else:
        return PrettyJsonResponse([item.model_dump(include={'id', 'name', 'rarity', 'icon'}) for item in items])