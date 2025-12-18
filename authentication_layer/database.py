from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
import os 
from dotenv import load_dotenv 

try : 
    #session creater and establishing a database connection 
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL") 
    engine = create_engine(DATABASE_URL)
    Sessionmaker = sessionmaker(autocommit = False,autoflush=False,bind= engine)
    #base is a class which we inherit the declarative base from pre written code of sqlalchemy and help 
    # us write and create models or orms 
    Base = declarative_base()
except Exception as e: 
    print("Error occurs  in the establishment of the database connection  :",e)

def get_db(): 
    db =  Sessionmaker()
    try : 
        yield db 
    finally : 
        db.close()


    
