from sqlalchemy import Column, Text, Integer
from db.config import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn13 = Column(Text)
    author = Column("author", Text)
    bookformat = Column("bookformat", Text)
    description = Column("description", Text)
    genre = Column("genre", Text)
    img = Column("img", Text)
    isbn = Column("isbn", Text)
    link = Column("link", Text)
    pages = Column("pages", Text)
    rating = Column("rating", Text)
    reviews = Column("reviews", Text)
    title = Column("title", Text)
    totalratings = Column("totalratings", Text)

