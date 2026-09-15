from fastapi import FastAPI, Request, HTTPException
from sqlalchemy import text
import requests
import json
from urllib.parse import urlparse



def user_webhook(user,db):
    
    event=user.event
    url=user.target_url
    payload=user.payload
    payload1=json.dumps(user.payload)
    parsedurl=urlparse(url)
    
    print(parsedurl)
    
    if not parsedurl.scheme and not parsedurl.netloc:
        raise HTTPException(status_code=422,detail="invalid url")
    
    result=db.execute(
        text("INSERT INTO wehbook(event,target_url,payload) VALUES(:event,:target_url,:payload)"),
        {
            "event":event,
            "target_url":url,
            "payload":payload1
        }
    )
        
    db.commit()
    
    print(payload)
    print(type(payload))
    print(result)
    
    response=requests.post(url,json=payload)
    
    if response.status_code!=200:
        
        for i in range(0,3):
            response1=requests.post(url,json=payload)
            
            if response1.status_code==200:
                result1=db.execute(
                            text("Update TABLE wehbook SET status=:status WHERE id=:id"),
                            {
                                "status":"Success"
                                "id":wehbbok_id
                            }
                        )
                break
        if response1.status_code!=200:  
              result1=db.execute(
                        text("Update TABLE wehbook SET status=:status WHERE id=:id"),
                        {
                            "status":"failed"
                            "id":wehbbok_id
                        }
                    )
      
    
    return{
        "message":"webhook created successfully"
    }