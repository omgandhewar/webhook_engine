from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from urllib.parse import urlparse



def user_webhook(user,db):
    
    event=user.event
    url=user.target_url
    payload=user.payload
    
    parsedurl=urlparse(url)
    
    print(parsedurl)
    
    if not parsedurl.scheme and not parsedurl.netloc:
        raise HTTPException(status_code=422,detail="invalid url")
    
    db.execute(
        text("INSERT INTO webhook(event,target_url,payload) VALUES(:event,:target_url,:payload)"),
        {
            "event":event,
            "target_url":url,
            "payload":payload
        }
    )
        
    db.commit()
    
    return{
        "message":"webhook created successfully"
    }