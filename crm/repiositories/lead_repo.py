from sqlalchemy.orm import Session
from crm.models import Lead 

class LeadRepository : 
    def create(self,db: Session , lead : Lead) : 
        try :
            db.add(lead) 
            db.commit()
            db.refresh(lead)
            return lead 
        except Exception as e : 
            print(f"Error occured at the service {e}")

    def  get_by_id(self,db:Session,lead_id  :int) :
        return db.query(Lead).filter(Lead.id == lead_id).first()
    
    def get_by_emial(self,db:Session,emial : str):
        return db.query(Lead).filter(Lead.email == emial).first()
    
    def get_by_owner(self,db:Session, owner_id : int) : 
        return db.query(Lead).filter(Lead.owner_id == owner_id).first()
    
    
    
