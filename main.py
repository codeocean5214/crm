#this is the intial lib set up for the authemtication layer
from fastapi import FastAPI, Depends, HTTPException , status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from authentication_layer import auth,schemas,database,models
from authentication_layer.database import get_db , engine
import uvicorn as uv 
import logging 
#crete the database tables and getting the database engine  
models.Base.metadata.create_all(bind = engine )
app = FastAPI()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
#writting the api end  point 
#new user registration endpoint
@app.post("/register",response_model = schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)) : 
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    if len(user.password) > 72:
        raise HTTPException(status_code=400, detail="Password too long")
    
    truncated_password = user.password.encode('utf-8')[:72].decode('utf-8', errors='ignore')
    hashed_password = auth.get_password_hash(truncated_password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password  
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating user")
#write the token generation endpoint 
@app.post("/token",response_model = schemas.Token) 
def login_for_access_token(form_data : OAuth2PasswordRequestForm  = Depends(),db  : Session = Depends(get_db)) :
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password,user.password)  : 
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate":"Bearer"
                     })
    
    try : 
        acess_token = auth .create_access_token(data = {"sub": user.username })
    except Exception as e :
        print("Error : ",e)
        raise HTTPException(status_code=500,detail="Internal server error")
    return {"access_token": acess_token , "token_type":"bearer"}
async def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    username = auth.verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/me", response_model = schemas.User)
def read_users_me(current_user: schemas.User = Depends(get_current_user)): #first we are verifying the token and then getting the current user thas all 
    return current_user

#SETTING UP THE VIDEO ENDPOINT
@app.post("/setup-admin", response_model = schemas.Admin)
def setup_admin(admin : schemas.AdminCreate, db  : Session = Depends(get_db)): 
    """Willl be adding additonal admin login security features once its done and compling properly  something like 
    2FA or OTP based login for the admin users
    """
    db_admin = db.query(models.Admin).filter(models.Admin.admin_name == admin.username).first()
    if db_admin : 
        raise HTTPException(status_code=400, detail="Admin already exists")
    """if len(admin.password) > 72 : 
        raise HTTPException(status_code=400, detail="Password too long")"""
    truncated_password = admin.password.encode('utf-8')[:72].decode('utf-8', errors='ignore')
    hashed_password = auth.get_password_hash(truncated_password)
    try : 
        new_admin = models.Admin(
            admin_name = admin.username,
            admin_login_mail = admin.email,
            admin_password = hashed_password
        )
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    except Exception as e :
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating admin user")
#token generation endpoint for the user 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  #maintain the logging file
        logging.StreamHandler() 
    ]
)
@app.post("/admin/token",response_model = schemas.Token) 
def login_for_access_token(form_data : OAuth2PasswordRequestForm  = Depends(),db  : Session = Depends(get_db)) :
    user = db.query(models.Admin).filter(models.Admin.admin_name == form_data.username).first()
    if not user or not auth.verify_password(form_data.password,user.password)  : 
        logging.warning(f"Failed login attempt for admin: {form_data.username}")
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate":"Bearer"
                     })
    
    try : 
        access_token = auth .create_access_token(data = {"sub": user.admin_name })
    except Exception as e :
        print("Error : ",e)
        raise HTTPException(status_code=500,detail="Internal server error")
    return {"access_token": access_token  , "token_type":"bearer"}
async def  get_current_admin(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    username = auth.verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    admin = db.query(models.Admin).filter(models.Admin.admin_name == username).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin
@app.get("/admin/me", response_model = schemas.Admin)
def read_admins_me(current_admins: schemas.Admin = Depends(get_current_admin)): #first we are verifying the token and then getting the current admin thas all 
    return current_admins
if __name__ == "__main__" : 
    uv.run(app, host="127.0.0.1", port=8000)
#uvicorn main:app --reload
