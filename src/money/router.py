from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.money.models import MoneyUser
from src.money.schema import MoneyCreate

money = APIRouter(prefix='/money',
                  tags=['Money'])

@money.get("/")
async def get_money_user(sessions: AsyncSession = Depends(get_async_session)):
    query = select(MoneyUser)
    result = await sessions.execute(query)
    return {"result": result.mappings().all()}

@money.post("/")
async def add_money(money: MoneyCreate, sessions: AsyncSession = Depends(get_async_session)):
    stmt = insert(MoneyUser).values(**money.dict())
    await sessions.execute(stmt)
    await sessions.commit()
    return {"result": 200}
