
from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter(include_in_schema=False)


@router.get('/')
async def home_route():
    return RedirectResponse('https://api.toweroffantasy.info/docs')