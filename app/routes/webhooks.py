from fastapi import FastAPI,APIRouter
from schemas.webhook import users
from services.webhook_service import user_webhook


router=APIRouter()


@router.post("/webhook")
def webhook(user:users):
    return user_webhook(user)
    
    