from fastapi import APIRouter
from app.schemas.redis_schemas import (
    StringValueRequest,
    IntegerValueRequest,
    ExpireRequest,
    IncrementRequest,
    HashRequest,
    ListRequest,
)
from app.services.redis_service import RedisService

router = APIRouter()
service = RedisService()


# STRING
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


# INTEGER
@router.post("/integers/{key}")
def create_or_update_integer(key: str, request: IntegerValueRequest):
    return service.create_or_update_integer(key, request.value)


@router.get("/integers/{key}")
def get_integer(key: str):
    return service.get_integer(key)


@router.delete("/integers/{key}")
def delete_integer(key: str):
    return service.delete_key(key)


@router.post("/integers/{key}/expire")
def expire_integer(key: str, request: ExpireRequest):
    return service.expire_key(key, request.seconds)


@router.post("/integers/{key}/incr")
def increment_integer(key: str, request: IncrementRequest):
    return service.increment_integer(key, request.amount)


# HASH
@router.post("/hashes/{key}")
def create_or_update_hash(key: str, request: HashRequest):
    return service.create_or_update_hash(key, request.values)


@router.get("/hashes/{key}")
def get_hash(key: str):
    return service.get_hash(key)


@router.get("/hashes/{key}/{field}")
def get_hash_field(key: str, field: str):
    return service.get_hash_field(key, field)


@router.delete("/hashes/{key}")
def delete_hash(key: str):
    return service.delete_hash(key)


@router.delete("/hashes/{key}/{field}")
def delete_hash_field(key: str, field: str):
    return service.delete_hash_field(key, field)


@router.post("/hashes/{key}/expire")
def expire_hash(key: str, request: ExpireRequest):
    return service.expire_key(key, request.seconds)


@router.post("/hashes/{key}/{field}/incr")
def increment_hash_field(key: str, field: str, request: IncrementRequest):
    return service.increment_hash_field(key, field, request.amount)


# LIST
@router.post("/lists/{key}")
def create_list(key: str, request: ListRequest):
    return service.create_list(key, request.values)


@router.get("/lists/{key}")
def get_list(key: str):
    return service.get_list(key)


@router.put("/lists/{key}")
def update_list(key: str, request: ListRequest):
    return service.update_list(key, request.values)


@router.delete("/lists/{key}")
def delete_list(key: str):
    return service.delete_list(key)


@router.post("/lists/{key}/expire")
def expire_list(key: str, request: ExpireRequest):
    return service.expire_key(key, request.seconds)


@router.post("/lists/{key}/incr/{index}")
def increment_list_item(key: str, index: int, request: IncrementRequest):
    return service.increment_list_item(key, index, request.amount)
