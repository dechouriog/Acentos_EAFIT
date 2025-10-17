from sqlalchemy import Column, Integer, Text
from db.config import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    user_type = Column("user_type", Text, nullable=False) 
    name = Column("name", Text, nullable=False)
    username = Column("username", Text, unique=True, nullable=False)
    password = Column("password", Text, nullable=False)
    address = Column("address", Text)
    phone_number = Column("phone_number", Text)
    mail = Column("mail", Text, unique=True)
