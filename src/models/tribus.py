from sqlalchemy import Integer,String
from sqlalchemy.sql.schema import Column
from ..database import Base
from sqlalchemy.orm import relationship
from .associated import association_table
import pydantic

class Config:
    arbitrary_types_allowed = True

@pydantic.dataclasses.dataclass(config=Config)
class Tribus(Base):
    __tablename__ = 'tribus'

    id_tribus = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    users = relationship(
        "User", secondary=association_table, back_populates="tribus"
    )