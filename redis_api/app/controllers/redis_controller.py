from fastapi import APIRouter
from app.schemas.redis_schemas import StringValueRequest, ExpireRequest, IncrementRequest
from app.services.redis_service import RedisService

router = APIRouter()
service = RedisService()


@router.post("/strings/{key}")
def create_or_update_string(key: str, request: StringValueRequest):
    return service.create_or_update_string(key, request.value)


@router.get("/strings/{key}")
def get_string(key: str):
    return service.get_string(key)


@router.delete("/strings/{key}")
def delete_string(key: str):
    return service.delete_key(key)


@router.post("/strings/{key}/expire")
def expire_string(key: str, request: ExpireRequest):
    return service.expire_key(key, request.seconds)


@router.post("/strings/{key}/incr")
def increment_string(key: str, request: IncrementRequest):
    return service.increment_key(key, request.amount)
