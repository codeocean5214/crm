from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session  

from crm.schemas import DealCreate,Dealsupdate 
from crm.services.deal_service  import DealServices  
from authentication_layer.dependcies import get_current_admin 
from authentication_layer.database import get_db 

router = APIRouter(prefix="/deals",tags = ["Deals"])
service = DealServices()

@router.post("/")
def create_post(payload : DealCreate , db: Session =  Depends(get_db),admin = Depends(get_current_admin)):
    return service.create_deal(db, payload.customer_id,  payload.amount, admin)


@router.patch("/{deal_id}/stage") 
def advance_stage(deal_id : int , payload : Dealsupdate  , db: Session = Depends(get_db)) : 
    return service.advance_stage(db,deal_id,payload.stage)