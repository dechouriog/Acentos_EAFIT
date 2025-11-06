from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from db.config import get_db
from controllers import cart_controller

# Prefijo del carrito
router = APIRouter(prefix="/cart")


# ---------------------------------------------------
# MOSTRAR CARRITO
# ---------------------------------------------------
@router.get("/")
def show_cart(request: Request, db: Session = Depends(get_db)):
    return cart_controller.show_cart(request, db)


# ---------------------------------------------------
# AGREGAR AL CARRITO
# ---------------------------------------------------
@router.post("/add/{book_id}")
def add_to_cart(book_id: int, request: Request, db: Session = Depends(get_db)):
    return cart_controller.add_to_cart(book_id, request, db)


# ---------------------------------------------------
# ELIMINAR ITEM
# ---------------------------------------------------
@router.post("/remove/{book_id}")
def remove_from_cart(book_id: int, request: Request, db: Session = Depends(get_db)):
    return cart_controller.remove_from_cart(book_id, request, db)


# ---------------------------------------------------
# PAGAR
# ---------------------------------------------------
@router.post("/pay")
def pay_cart(request: Request, db: Session = Depends(get_db)):
    return cart_controller.pay_cart(request, db)
