from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crm.services.task_service import TaskService
from authentication_layer.dependcies import  get_current_admin
from crm.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])
service = TaskService()


@router.get("/my")
def my_tasks(
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    return service.get_my_pending_tasks(db, admin.id)