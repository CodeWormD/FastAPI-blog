from fastapi import APIRouter

from .posts.router import router as post_router
from .groups.router import router as group_router

router = APIRouter(
    prefix='/api'
)

router.include_router(post_router)
router.include_router(group_router)