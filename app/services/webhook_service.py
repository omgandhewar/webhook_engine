from fastapi import FastAPI, HTTPException
from urllib.parse import urlparse



def user_webhook(user):
    
    url=user.target_url
    
    parsedurl=urlparse(url)
    
    print(parsedurl)
    
    if not parsedurl.scheme and not parsedurl.netloc:
        raise HTTPException(status_code=422,detail="invalid url")
        