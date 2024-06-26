from contextlib import asynccontextmanager

import aioredis
from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend, fastapi_users, current_user
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schema import UserRead, UserCreate
from src.operation.router import router as router_operation
from src.money.router import money as router_money
from src.tasks.router import router as router_tasks

app = FastAPI(title='test')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)
app.include_router(router_money)
app.include_router(router_tasks)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello"

# при старте приложении вызывается данная функция
@app.on_event("startup")
async def startup_event():
    # идет подключение к редису
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responces=True)
    # инициализация класса, после этого можем использовать декоратор cache(expire=30) и сколько секунд
    # будет храниться кэш
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
