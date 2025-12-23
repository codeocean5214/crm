from sqlalchemy.orm import Session
from crm.models import Task

class TaskRepository:

    def create(self, db: Session, task: Task):
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def get_pending_by_user(self, db: Session, user_id: int):
        return (
            db.query(Task)
            .filter(
                Task.assigned_to == user_id,
                Task.status == "pending"
            )
            .all()
        )
