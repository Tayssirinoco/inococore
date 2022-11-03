from typing import List
from ..models.user import User
from pydantic import BaseModel



class TribusBase(BaseModel):   
    name : str
    
    class Config:
        orm_mode = True

class TribusSchema(TribusBase):
    users_re : List[User]