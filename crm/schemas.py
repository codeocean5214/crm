from pydantic import BaseModel ,EmailStr, Field
from constants import LeadStatus,ContactMethod, DealStage
from datetime import datetime
from typing import Optional #null values ke liye

class ORMbase(BaseModel):
    class Config : 
        orm_mode = True

# three schemas for each model creade , update and  response schema
class LeadCreate(ORMbase) : 
    name  : str 
    email : EmailStr
    phone_number : int 
    contact_method : ContactMethod
    owner_id : int

class LeadUpdate(ORMbase) : 
    status : LeadStatus

class LeadResponse(ORMbase) : 
    id : int
    name  : str 
    email : EmailStr
    phone_number : int 
    contact_method : ContactMethod
    owner_id : int
    status : LeadStatus

#customer is not created directly beacuse lead genrate ussi sie hoti hai 
class CustomerResponse(ORMbase) : 
    id : int
    name  : str 
    email : EmailStr
    source_lead_id : int
    created_at : datetime


#WRITTING THE SIMILAR FOR THE DEAL SCHEMA 
class DealCreate(ORMbase) : 
    customer_id : int
    amount : float
    stage : DealStage
    owner_id : int

class Dealsupdate(ORMbase)  : 
    stage  : DealStage 
    amount : Optional[float] = None

class DealResponse(ORMbase): 
    id: int
    customer_id: int
    amount: float
    stage: DealStage
    probability: Optional[float] = None
    expected_value: Optional[float] = None
    created_at: datetime

#writing the task schema for task management 
class TaskCreate(ORMbase) : 
    entity_type : str 
    entity_id : int
    title : str 
    description : Optional[str] = None
    due_date : Optional[datetime] = None
    assigned_to : int
class TaskUpdate(ORMbase) : 
    status : str

class TaskResponse(ORMbase) :
    id : int
    entity_type : str 
    entity_id : int
    title : str 
    description : Optional[str] = None
    due_date : datetime
    status : str
    assigned_to : int
    created_at : datetime
