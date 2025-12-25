#repositries are written are for the purpose of interacting with the database, we could 
# used normal functions bto access db featues in the  main but repo proivdes more decentralisation
from sqlalchemy.orm import Session  
from crm.models import Customer  

class CustomerRepo : 

    #operation to create a customer in db 
    def create(self,db: Session , customer : Customer) : 
        try : 
            db.add(customer)
            db.commit(customer)
            db.refresh(customer)
            return customer
        except Exception as e  :
            print(f"Error ocured during repository operation {e}")
    #getting options 
    def get_customer_emial(self,db:Session,email : str) : 
        return db.query(Customer).filter(Customer.email  == email).first()
    #internal implementation 
    def get_customer_by_id(self,db:Session,customer_id: int) : 
        return db.query(Customer).filter(Customer.id == customer_id).first()
    

