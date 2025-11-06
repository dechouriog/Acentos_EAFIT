from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.config import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id_user"), nullable=False)  # 👈 correcto
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    quantity = Column(Integer, default=1)

    book = relationship("Book", back_populates="cart_items")
