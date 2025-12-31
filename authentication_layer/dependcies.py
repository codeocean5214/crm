from fastapi import HTTPException, Depends, status 
from sqlalchemy.orm import Session 
from fastapi.security import OAuth2PasswordBearer
from authentication_layer.auth import verify_token 
from authentication_layer.models import Admin 
import json 

from authentication_layer.database import get_db
#implementing the caching layer in the auth layer using redis

from crm.redis_client import redis_client 
async def get_redis() : 
    return redis_client 
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def  get_current_admin(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    username = verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    #redis database check (we will check for which user name is present in the redis ram database or not)
    key  = f"admin :{username}"
    cached_adm = redis_client.get(key) 
    if cached_adm : 
        return json.loads(cached_adm)

    admin = db.query(Admin).filter(Admin.admin_name == username).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    #storing the admin  in redis database 
    redis_client.setex(key, 3600,
                       json.dumps({
                "id" : admin.id, 
                "admin_name" : admin.admin_name })
    )
    return admin