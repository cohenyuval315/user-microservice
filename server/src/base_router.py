from fastapi import APIRouter
from server.src.common.common_router import common_router
from server.src.users.user_router import user_router
from server.src.access_control.access_control_router import access_control_router

base_router = APIRouter()

base_router.include_router(
    router=common_router,
    prefix="",
)

base_router.include_router(
    router=user_router,
    prefix="/users"
)

base_router.include_router(
    router=access_control_router,
    prefix="/ac"
)


