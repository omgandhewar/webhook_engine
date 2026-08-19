from fastapi import FastAPI, Depends, APIRouter
from schemas.webhook import users
from db.database import get_db
from services.webhook_service import user_webhook


router=APIRouter()


@router.post("/webhook")
def webhook(user:users,db=Depends(get_db)):
    return user_webhook(user,db)
    
    