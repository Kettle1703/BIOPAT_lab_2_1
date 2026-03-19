from pydantic import BaseModel


class StringValueRequest(BaseModel):
    value: str


class IntegerValueRequest(BaseModel):
    value: int


class ExpireRequest(BaseModel):
    seconds: int


class IncrementRequest(BaseModel):
    amount: int = 1


class HashRequest(BaseModel):
    values: dict[str, str]


class ListRequest(BaseModel):
    values: list[str]
