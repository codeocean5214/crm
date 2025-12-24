#so the only job of the customer is to decide wheather the deals is converted or not  
from fastapi import APIRouter,Depends 
from sqlalchemy.orm import Session 

from crm.services.lead_service import LeadService 
from crm.services.customer_service import Customer_Service
from authentication_layer.database import get_db 
from main import get_current_admin 

router =  APIRouter( prefix="/customer",tags=['customer']) 
customer_service= Customer_Service ()
lead_service = LeadService()

@router.post("/convert/{lead_id}")
def convert_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    lead = lead_service.get_lead_for_conversion(db, lead_id)
    return customer_service.convert_from_lead(db, lead)