from fastapi import FastAPI
from app.controllers.redis_controller import router as redis_router

app = FastAPI(title="Redis HTTP API")

app.include_router(redis_router)
