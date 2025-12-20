from sqlalchemy import Column , String, Integer
from authentication_layer.database import Base 

#creating the user class
class User(Base):
    __tablename__  = "users"
    id  = Column(Integer,primary_key=True , index = True)
    username = Column(String,unique=True,index=True)
    email = Column(String,unique=True,index = True)
    password = Column(String) #iit will sotrwed in the form of hash 
#creating the admin class 
#for thhe storing data for the admins  
class Admin(Base) : 
    __tablename__ = "admin_data" 
    id = Column(Integer,primary_key = True , index= False) #LESS ADMIN DATA SO NO NEED FOR THE CHUNCKING OF THE BLOCS 
    admin_name = Column(String,unique=True,index= True)
    admin_login_mail  = Column(String,unique=True,index = True)
    admin_password  = Column(String)

#creating the otp table for storing the otp data
class OptData(Base): 
    __tablename__  = "opt_data"
    id  = Column(Integer,primary_key=True , index = True)
    email = Column(String,unique=True,index = True)
    otp  = Column(String)
    timestamp = Column(String)

