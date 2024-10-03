from fastapi import FastAPI

from fastapi_users import FastAPIUsers

from src.cat.router import router as router_cat

app = FastAPI()

app.include_router(router_cat)