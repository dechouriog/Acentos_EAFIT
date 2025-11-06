from sqlalchemy import Column, Text, Integer
from db.config import Base  # ✅ usa la misma Base del proyecto
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn13 = Column(Text)
    author = Column(Text)
    bookformat = Column(Text)
    description = Column(Text)
    genre = Column(Text)
    img = Column(Text)
    isbn = Column(Text)
    link = Column(Text)
    pages = Column(Text)
    rating = Column(Text)
    stock = Column(Integer)
    title = Column(Text)
    totalratings = Column(Text)
    price = Column(Integer)

    # ✅ relación con el carrito
    cart_items = relationship(
        "CartItem", back_populates="book", cascade="all, delete-orphan"
    )
