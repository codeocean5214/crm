from fastapi import APIRouter,Depends 
from sqlalchemy.orm import Session  
from crm.schemas import LeadCreate,LeadResponse 
from crm.services