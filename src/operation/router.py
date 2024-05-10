from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operation.models import Operation
from src.operation.schema import OperationCreate

router = APIRouter(prefix='/operations',
                   tags=['Operation'])

@router.get("/")
async def get_specific_operations(operation_type: str, sessions: AsyncSession = Depends(get_async_session)):
    query = select(Operation).where(Operation.type == operation_type).order_by(Operation.date)
    result = await sessions.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_operation(new_operation: OperationCreate, sessions: AsyncSession = Depends(get_async_session)):
    # чтобы словарь развернулся, и параметры отправились в формате id=2, type=..  и так далее
    statement = insert(Operation).values(**new_operation.dict())
    await sessions.execute(statement)
    await sessions.commit()
    return {"status_code": 200}