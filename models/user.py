from sqlalchemy import Column, Integer, Text
from db.config import Base


class User(Base):
    __tablename__ = "User"  # Mayúscula, confirmado

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    user_type = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    username = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    address = Column(Text)
    phone_number = Column(Text)
    mail = Column(Text, unique=True)
