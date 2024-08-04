from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.router import router as router_api

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_api)
