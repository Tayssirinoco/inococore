from fastapi import FastAPI, Depends
from .schemas.tribus import TribusBase, TribusSchema
from sqlalchemy.orm import Session, joinedload
from .database import get_db
from .models.user import User
from .models.tribus import Tribus

app = FastAPI()

@app.get("/")
def get(db: Session = Depends(get_db)):
    b1 = db.query(Tribus).options(joinedload(Tribus.users_re)).where(Tribus.id_tribus==1).one()
    b1_schema = TribusSchema.from_orm(b1)
    print(b1_schema.json())