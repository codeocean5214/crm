from fastapi import HTTPException 
from crm.models import Customer 
from sqlalchemy.orm import Session 
from  crm.constants import LeadStatus 

class  Customer_Service : 
    def convert_from_lead(self,db:Session,lead) : 
        if lead.status != LeadStatus.qualified : 
            raise HTTPException(
                status_code= 400, 
                detail = "Only qualified leads can be converted"
            )
        #customer detail 
        customer  = Customer(
            name = lead.name, 
            email = lead.email, 
            source_lead_id = lead.id
        )
        lead.status  = LeadStatus.converted
        try : 
            
            db.add(customer)
            db.commit()
            db.refresh(customer)

            return customer
        except Exception as e : 
            raise HTTPException(status_code=500 , detail=e)
        

