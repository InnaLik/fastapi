from typing import List

from fastapi import FastAPI
from pydantic import Field, BaseModel

app = FastAPI(title='Tradding App')

test_bd_user = [{"id": 1, "role": "admin", "name": "Bob1"},
                {"id": 2, "role": "admin", "name": "Bob2"},
                {"id": 3, "role": "admin", "name": "Bob3"},
                {"id": 4, "role": "admin", "name": "Bob4"}]

test2_bd_user = [{"id": 1, "role": "admin", "name": "Bob1"},
                 {"id": 2, "role": "admin", "name": "Bob2"},
                 {"id": 3, "role": "admin", "name": "Bob3"},
                 {"id": 4, "role": "admin", "name": "Bob4"}]

test_bd_trades = [{"id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
                  {"id": 2, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
                  {"id": 3, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12}]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [i for i in test_bd_user if i["id"] == user_id]

class Trade(BaseModel):
    id: int
    currency: str = Field(max_length=10)
    side: str
    price: int = Field(gt=0)
    amount: float

@app.post("/trades/")
def add_trades(trades: List[Trade]):
    test_bd_trades.extend(trades)
    return {"ststus": 200,
            "data": test_bd_trades}
