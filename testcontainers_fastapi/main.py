from fastapi import FastAPI
from .router import router as export_router

app = FastAPI()

app.include_router(export_router)
