from sqlalchemy import ForeignKey, Integer,Table
from sqlalchemy.sql.schema import Column
from ..database import Base


association_table = Table(
    "associated",
    Base.metadata,
    Column("id_user", Integer, ForeignKey("users.id_user"), primary_key=True),
    Column("id_tribus", Integer, ForeignKey("tribus.id_tribus"), primary_key=True),
)