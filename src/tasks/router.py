from fastapi import APIRouter, Depends, BackgroundTasks

from src.auth.base_config import current_user
from src.tasks.tasks import send_email_report_dashboard

router = APIRouter(prefix="/report",
                   tags=['report'])

# @router.get("/dashboard")
# def get_dasboard_report(user=Depends(current_user)):
#     # send_email_report_dashboard(user.username)
#     return {
#         "status": 200,
#         "data": "Письмо направлено",
#         "details": None
#     }


@router.get("/dashboard")
def get_dasboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    background_tasks.add_task(send_email_report_dashboard, user.username)
    # send_email_report_dashboard(user.username)
    return {
        "status": 200,
        "data": "Письмо направлено",
        "details": None
    }