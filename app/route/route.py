from fastapi import APIRouter
from .heroes import heroes_router
from .user import user_router

main_router = APIRouter()

main_router.include_router(heroes_router, prefix="/hero", tags=["Signup"], responses={404: {"description": "Not found"}})
main_router.include_router(user_router, prefix="/user", tags=["User"], responses={404: {"description": "Not found"}})