import datetime
from enum import Enum
from typing import List
from fastapi import FastAPI, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from pydantic import Field, BaseModel
from starlette.responses import JSONResponse

app = FastAPI(title='Tradding App')

test_bd_user = [{"id": 1, "role": "admin", "name": "Bob1",
                 "degree": [{"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}]},
                {"id": 2, "role": 1, "name": "Bob2"},
                {"id": 3, "role": "admin", "name": "Bob3"},
                {"id": 4, "role": "admin", "name": "Bob4"}]

test2_bd_user = [{"id": 1, "role": "admin", "name": "Bob1"},
                 {"id": 2, "role": "admin", "name": "Bob2"},
                 {"id": 3, "role": "admin", "name": "Bob3"},
                 {"id": 4, "role": "admin", "name": "Bob4"}]

test_bd_trades = [{"id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
                  {"id": 2, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
                  {"id": 3, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12}]

@app.exception_handler(ResponseValidationError)
async def validation_exc_hand(request: Request, exc: ResponseValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=jsonable_encoder({"detail": exc.errors()}))

class DegreeEnum(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime.datetime
    type_degree: DegreeEnum


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: list[Degree] = None


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [i for i in test_bd_user if i["id"] == user_id]


class Trade(BaseModel):
    id: int
    currency: str = Field(max_length=10)
    side: str
    price: int = Field(ge=0)
    amount: float


@app.post("/trades/")
def add_trades(trades: List[Trade]):
    test_bd_trades.extend(trades)
    return {"ststus": 200,
            "data": test_bd_trades}
