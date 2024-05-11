from pydantic import BaseModel, Field


class MoneyCreate(BaseModel):
    id: int
    name: str = Field(max_length=100)
    type_operation: str
    amount: int
