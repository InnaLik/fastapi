from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.auth.models import User
from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# url нашей бд
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



class Base(DeclarativeBase):
    pass


# точка входа алхимии в наше приложение
engine = create_async_engine(DATABASE_URL)
# создание сессии
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# получение асинхронной сессии
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session




