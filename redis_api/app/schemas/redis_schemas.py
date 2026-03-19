from pydantic import BaseModel


class StringValueRequest(BaseModel):
    value: str


class ExpireRequest(BaseModel):
    seconds: int


class IncrementRequest(BaseModel):
    amount: int = 1
