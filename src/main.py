from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend, fastapi_users, current_user
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schema import UserRead, UserCreate
from src.operation.router import router as router_operation

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

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"




@app.get("/unprotected-route")
def protected_route():
    return f"Hello"
