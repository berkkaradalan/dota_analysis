from fastapi import FastAPI, Depends
from app.route.route import main_router
from app.bootstrap.bootstrap import start_app

app = FastAPI()
app.include_router(main_router)

start_app()