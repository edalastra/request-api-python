from fastapi import FastAPI
from src.main.routes import users_routes

app = FastAPI()

app.include_router(users_routes)
