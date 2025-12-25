from fastapi import HTTPException, Depends, status 
from sqlalchemy.orm import Session 
from fastapi.security import OAuth2PasswordBearer
from authentication_layer.auth import verify_token 
from authentication_layer.models import Admin 
from authentication_layer.database import get_db
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def  get_current_admin(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    username = verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    admin = db.query(Admin).filter(Admin.admin_name == username).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin