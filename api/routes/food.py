
from fastapi import APIRouter

from api.enums import FOOD, LANGS, VERSIONS

from api.infra.entitys import Food, EntityBase
from api.infra.repository import FoodRepo

from api.core.response import PrettyJsonResponse


FOOD_REPO = FoodRepo()

router = APIRouter(prefix="/food", tags=["Food"])
METADATA = {
    'name': 'Food',
    'description': 'Food can provide buffs and recover HP, satiety, and stamina \n\n **DOES NOT CONTAINS CN DATA**',
    }


@router.get('/{id}', name='Get food', response_model=Food)
async def get_food(id: FOOD, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: food_id

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
        Food
    '''

    food = await FOOD_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(food.model_dump())
    else:
        return PrettyJsonResponse(food.model_dump(include={'id', 'name', 'icon', 'quality', 'stars'}))


@router.get('', name='All foods', response_model=list[Food])
async def get_all_foods(lang: LANGS = LANGS('en'), include: bool = False):
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
        List[Food]
    '''

    foods = await FOOD_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([food.model_dump() for food in foods])
    else:
        return PrettyJsonResponse([food.model_dump(include={'id', 'name', 'icon', 'quality', 'stars'}) for food in foods])
    