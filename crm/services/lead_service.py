#the lead service  has a simple functionality lead -> contacted -> qualified -> converted or lost 
#this  service codes the following buisness logic in the service  

from fastapi import HTTPException
from sqlalchemy.orm import Session 
from crm.models import Lead 
from crm.constants import LeadStatus
from crm.repiositories.lead_repo import LeadRepository 

class LeadService : 
    def __init__(self) : 
        self.repo = LeadRepository()

    def create_lead(self,db:Session,payload  : dict, admin ) : 
        if self.repo.get_by_emial(db,payload.email) : 
            raise HTTPException(status_code=400, detail="Lead already exists")
        lead  = Lead(
            name  = payload.name , 
            email = payload.email, 
             phone=payload.phone,
            status=LeadStatus.new,
            owner_id=admin.id

        )
        return self.repo.create(db,lead)
    
    def mark_contact(self,db:Session,lead_id  : int) :
        lead = self.repo.get_by_id(db,lead_id)  
        if not lead : 
            raise HTTPException(404,detail="LEAD DOESNOT EXIST OR WRONG ID")
        if lead.status !=  LeadStatus.new : 
            raise HTTPException(400,detail="only new can be contacted")
        try  : 
            lead.status = LeadStatus.contacted 
            db.commit()
            return lead 
        except Exception as e  : 
            print(f"error : { e}")
    
    def qualify_lead(self,db:Session,lead_id  : int) :
        lead = self.repo.get_by_id(db,lead_id)  
        if not lead : 
            raise HTTPException(404,detail="LEAD DOESNOT EXIST OR WRONG ID")
        if lead.status !=  LeadStatus.contacted : 
            raise HTTPException(400,detail="Contact to karo bhai")
        try  : 
            lead.status = LeadStatus.qualified   
            db.commit()
            return lead 
        except Exception as e  : 
            print(f"error : { e}")

    def mark_lost(self,db:Session,lead_id  : int) :
        lead = self.repo.get_by_id(db,lead_id)  
        if not lead : 
            raise HTTPException(404,detail="LEAD DOESNOT EXIST OR WRONG ID")
        if lead.status ==  LeadStatus.converted : 
            raise HTTPException(400,detail="Already converted")
        try  : 
            lead.status = LeadStatus.lost   
            db.commit()
            return lead 
        except Exception as e  : 
            print(f"error : { e}")

    def get_lead_for_conversion(self, db: Session, lead_id: int):
        lead = self.repo.get_by_id(db, lead_id)
        if not lead:
            raise HTTPException(404, "Lead not found")

        if lead.status != LeadStatus.qualified:
            raise HTTPException(
                400,
                "Only qualified leads can be converted"
            )

        return lead   
    