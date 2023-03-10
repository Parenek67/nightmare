from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    login = Column(String)
    password = Column(String)