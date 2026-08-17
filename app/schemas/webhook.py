from pydantic import BaseModel


class users(BaseModel):
    event:str
    target_url:str
    payload:dict