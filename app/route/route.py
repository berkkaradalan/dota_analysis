from fastapi import APIRouter
from .game import game_router
from .heroes import heroes_router
from .user import user_router
from .match import match_router

main_router = APIRouter()

main_router.include_router(heroes_router, prefix="/hero", tags=["Signup"], responses={404: {"description": "Not found"}})
main_router.include_router(user_router, prefix="/user", tags=["User"], responses={404: {"description": "Not found"}})
main_router.include_router(match_router, prefix="/match", tags=["Match"], responses={404: {"description": "Not found"}})
main_router.include_router(game_router, prefix="/game", tags=["Game"], responses={404: {"description": "Not found"}})