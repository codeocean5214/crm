from crm.repiositories.task_repo import TaskRepository
from crm.models import Task 
from datetime import datetime,timedelta

class TaskService : 
    def __init__(self) : 
        self.repo = TaskRepository()
    #abhi kie mvp mie follow up task daal deta hun
    
    def create_folllow_up( self , db, entity_type : str , entity_id : int, 
                         admin_id:int,days: int = 2 ) : 
        task = Task(
            entity_type=entity_type,
            entity_id=entity_id,
            title="Follow-up",
            due_date=datetime.utcnow() + timedelta(days=days),
            assigned_to=admin_id
        )

        return self.repo.create(db, task)
    
    def get_my_pending_tasks(self, db, admin_id: int):
        return self.repo.get_pending_by_user(db, admin_id)