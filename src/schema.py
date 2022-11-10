from typing import List
from pydantic import BaseModel
from pydantic.schema import Optional

class UserBase(BaseModel):   
    first_name  : str
    last_name : Optional[str] 
    seniority_lvl : int
    associated : bool
    badge : str
    manager_id : Optional[int] 
    class Config:
        orm_mode = True

class TribusBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class TribusSchema(TribusBase):
    users: List[UserBase]
    
class UserSchema(UserBase):
    tribus : List[TribusBase] 
    