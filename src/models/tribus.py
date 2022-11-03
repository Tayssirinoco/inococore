from sqlalchemy import Integer,String
from sqlalchemy.sql.schema import Column
from ..database import Base
from .associated import association_table
from sqlalchemy.orm import relationship
import pydantic

class Config:
    arbitrary_types_allowed = True

@pydantic.dataclasses.dataclass(config=Config)
class Tribus(Base):
    __tablename__ = 'tribus'

    id_tribus = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    users_re = relationship(
        "User", secondary=association_table, back_populates="tribus_re"
    )