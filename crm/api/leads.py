from fastapi import APIRouter,Depends 
from sqlalchemy.orm import Session  
from crm.schemas import LeadCreate,LeadResponse 
from crm.services.lead_service import LeadService 
from main import get_current_admin 
from authentication_layer.database import get_db 

router = APIRouter(prefix="/leads",tags=["Lead"])
service = LeadService()

@router.post("/",response_model=LeadResponse) 
def create_lead(payload = Depends(LeadCreate),db : Session  = Depends(get_db), admin = Depends(get_current_admin)) : 
    return service.create_lead(db,payload,admin) 

@router.patch("/{lead_id}/contact")  
def mark_contact(lead_id : int, db: Session =  Depends(get_db)) : 
    return service.mark_contact(lead_id,db)

@router.patch("/{lead_id}/qualify")  
def mark_qualified(lead_id : int, db: Session =  Depends(get_db)) : 
    return service.qualify_lead(lead_id,db)

@router.patch("/{lead_id}/lost")  
def mark_lost(lead_id : int, db: Session =  Depends(get_db)) : 
    return service.mark_lost(lead_id,db)


