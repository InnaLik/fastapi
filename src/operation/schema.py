import datetime

from pydantic import Field, BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str = Field(default=None)
    date: datetime.datetime
    type: str

