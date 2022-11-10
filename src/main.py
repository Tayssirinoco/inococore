from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, joinedload

from .schema import TribusSchema, UserSchema
from .database import get_db
from .models.tribus import Tribus
from .models.user import User
app = FastAPI()

@app.get("/tribus")
def get(db: Session = Depends(get_db)):
    b1 = db.query(Tribus).options(joinedload(Tribus.users)).where(Tribus.id_tribus==1).one()
    b1_schema = TribusSchema.from_orm(b1)
    return b1_schema

@app.get("/users")
def get(db: Session = Depends(get_db)):
    b1 = db.query(User).options(joinedload(User.tribus)).where(User.id_user==1).one()
    b1_schema = UserSchema.from_orm(b1)
    return b1_schema

