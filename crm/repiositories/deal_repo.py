from sqlalchemy.orm import Session 
from crm.models import Deal

class DealRepository  : 
    def create(self,db:Session,deal : Deal): 
        db.add(deal)
        db.commit()
        db.refresh(deal)
        return deal 
    
    def get_deal_by_id(self,db:Session,deal_id : int) : 
        return db.query(Deal).filter(Deal.id == deal_id).first()
    
    def get_deal_active_customer(self,db:Session,customer_id : int):
        return db.query(Deal).filter(Deal.customer_id == customer_id,
                                     Deal.stage.notin_(['won','lost']) ).first()
    
    
        

