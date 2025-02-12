from fastapi import FastAPI, Depends
from app.route.route import main_router
from app.bootstrap.bootstrap import start_app, env_variables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None)
app.include_router(main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=env_variables.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

start_app()