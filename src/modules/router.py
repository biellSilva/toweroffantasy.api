from fastapi import APIRouter

from src.modules.auth.controller import router as auth_router
from src.modules.banners.controller import router as banner_router
from src.modules.gifts.controller import router as gift_router
from src.modules.health.controller import router as health_router
from src.modules.matrices.controller import router as matrice_router
from src.modules.mounts.controller import router as mount_router
from src.modules.simulacra.controller import router as simulacra_router
from src.modules.users.controller import router as user_router
from src.modules.weapons.controller import router as weapon_router

router = APIRouter()

router.include_router(auth_router)
# Auth router is included first

router.include_router(user_router)
router.include_router(simulacra_router)
router.include_router(matrice_router)
router.include_router(weapon_router)
router.include_router(banner_router)
router.include_router(gift_router)
router.include_router(mount_router)
router.include_router(health_router)
