from typing import List
from ..models.tribus import Tribus
from pydantic import BaseModel

class UserBase(BaseModel):   
    first_name  : str
    last_name : str
    seniority_lvl : int
    associated : bool
    badge : str
    manager_id : int
    class Config:
        orm_mode = True

class UserSchema(UserBase):
    tribus_re : List[Tribus] 