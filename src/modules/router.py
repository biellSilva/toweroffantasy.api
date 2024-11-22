from fastapi import APIRouter

from src.modules.auth.controller import router as auth_router
from src.modules.matrices.controller import router as matrice_router
from src.modules.users.controller import router as user_router

router = APIRouter()

router.include_router(auth_router)
# Auth router is included first

router.include_router(user_router)
router.include_router(matrice_router)
