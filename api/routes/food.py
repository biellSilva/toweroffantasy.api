
from fastapi import APIRouter, Query, Path

from api.enums import FOOD, LANGS, VERSIONS

from api.infra.entitys import Food, EntityBase
from api.infra.repository import FoodRepo

from api.core.response import PrettyJsonResponse


FOOD_REPO = FoodRepo()

router = APIRouter(prefix="/food", tags=["Food"])
METADATA = {
    'name': 'Food',
    'description': 'Food can provide buffs and recover HP, satiety, and stamina \t\n DOES NOT CONTAINS CN DATA',
}

INCLUDE = {'id', 'name', 'icon', 'quality', 'stars'}


@router.get('/{id}', name='Get food', response_model=Food)
async def get_food(id: FOOD = Path(description='Food ID'), 
                   lang: LANGS = Query(LANGS('en'), description='Language code'), 
                   include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \t\n
        Food
    '''

    food = await FOOD_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(food.model_dump())
    else:
        return PrettyJsonResponse(food.model_dump(include=INCLUDE))


@router.get('', name='All foods', response_model=list[Food])
async def get_all_foods(lang: LANGS = Query(LANGS('en'), description='Language code'), 
                        include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \n
        List[Food]
    '''

    foods = await FOOD_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([food.model_dump() for food in foods])
    else:
        return PrettyJsonResponse([food.model_dump(include=INCLUDE) for food in foods])
    