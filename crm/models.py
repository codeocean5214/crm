#creating the data models and defining the tables
from sqlalchemy import Column , String , Integer , Enum, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship 
from datetime import datetime
from crm.database import Base
from crm.constants import LeadStatus, ContactMethod, DealStage
class Lead(Base): 
    __tablename__ = "leads"
    id = Column(Integer,primary_key= True, index = True)
    name  = Column(String,nullable= False)
    email = Column(String,unique = True , index = True)
    phone_number = Column(String,unique=True , index = True)
    status  = Column(Enum(LeadStatus),default=LeadStatus.new)
    contact_method = Column(Enum(ContactMethod),nullable= False) # this will store the preferred contact method and cannot be null 
    ownfer_id = Column(Integer, ForeignKey("admins.id"))
    created_at = Column(DateTime,default= datetime.utcnow)
    owner = relationship("Admin", back_populates="leads")

    #owner = relationship("ADMIN", back_populates="leads")

class Customer(Base) :
    __tablename__ = "customers"
    id = Column(Integer,primary_key= True, index = True)
    name  = Column(String,nullable= False)
    email = Column(String,unique = True , index = True)
    source_lead_id = Column(Integer, ForeignKey("leads.id")) # konsa sa contact konse lead se aya hai
    created_at = Column(DateTime,default= datetime.utcnow)
    lead = relationship("Lead", back_populates="customers")
    #lead = relationship("Lead", back_populates="customers")

#deal management table 
class Deal(Base) :
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    amount = Column(Float)
    stage = Column(Enum(DealStage))
    probability = Column(Float)
    expected_value = Column(Float)
    owner_id = Column(Integer, ForeignKey("admins.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

#the task data model for storing the tasks assigned to the sales team and acts as overall task management system
class Task(Base): 
    __tablename__  = "tasks"
    id = Column(Integer, primary_key=True)
    entity_type = Column(String) #lead , customer , deal
    entity_id = Column(Integer)
    title = Column(String,nullable = False)
    description  = Column(String)
    due_date = Column(DateTime) 
    status = Column(String,default="pending") #pending , completed , overdue
    assigned_to = Column(Integer, ForeignKey("admins.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
