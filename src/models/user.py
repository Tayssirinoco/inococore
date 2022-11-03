from sqlalchemy import ForeignKey, Integer,String, Boolean
from sqlalchemy.sql.schema import Column
from ..database import Base
from .associated import association_table
from sqlalchemy.orm import relationship
import pydantic

class Config:
    arbitrary_types_allowed = True

@pydantic.dataclasses.dataclass(config=Config)
class User(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    seniority_lvl = Column(Integer, nullable=False)
    associated = Column(Boolean, nullable=False)
    badge = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id_user"))
    #managed_users=relationship("User")
    tribus_re = relationship(
        "Tribus", secondary=association_table, back_populates="users_re"
    )