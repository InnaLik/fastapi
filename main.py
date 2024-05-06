from enum import Enum

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse

app = FastAPI(title='test')

class Deal_type(Enum):
    buy = "buy"
    sell = "sell"

class Deal(BaseModel):
    type_deal: Deal_type
    currency: str = Field(max_length=10)
    price: int = Field(ge=0)
    amount: int = Field(gt=0)


class User(BaseModel):
    id: int
    name: str
    role: str
    deal: Deal = None


db_seller = [{"id": 1, "name": "Inna", "role": "Seller", "deal": {"type_deal": "sell", "currency": "USD", "price": 1, "amount": -2}}]

@app.post("/trades/")
def get_trades(user: User):
    return user

@app.exception_handler(ResponseValidationError)
async def validation_exc_hand(request: Request, exc: ResponseValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=jsonable_encoder({"detail": exc.errors()}))