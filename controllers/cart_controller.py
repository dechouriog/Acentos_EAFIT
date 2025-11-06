from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models.books import Book
from models.cart import CartItem


templates = Jinja2Templates(directory="views")


# ---------------------------------------------------
# MOSTRAR CARRITO
# ---------------------------------------------------
def show_cart(request, db: Session):
    user = request.state.user
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    cart_items = db.query(CartItem).filter(CartItem.user_id == user.id_user).all()
    total = sum(item.book.price * item.quantity for item in cart_items)

    return templates.TemplateResponse(
        "cart.html", {"request": request, "cart_items": cart_items, "total": total}
    )


# ---------------------------------------------------
# AGREGAR LIBRO AL CARRITO
# ---------------------------------------------------
def add_to_cart(book_id: int, request, db: Session):
    user = request.state.user
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or book.stock <= 0:
        return RedirectResponse(url=f"/books/{book_id}", status_code=303)

    cart_item = (
        db.query(CartItem).filter_by(user_id=user.id_user, book_id=book_id).first()
    )

    if cart_item:
        cart_item.quantity += 1
    else:
        new_item = CartItem(user_id=user.id_user, book_id=book.id, quantity=1)
        db.add(new_item)

    db.commit()
    return RedirectResponse(url="/cart", status_code=303)


# ---------------------------------------------------
# ELIMINAR LIBRO DEL CARRITO
# ---------------------------------------------------
def remove_from_cart(book_id: int, request, db: Session):
    user = request.state.user
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    cart_item = (
        db.query(CartItem).filter_by(user_id=user.id_user, book_id=book_id).first()
    )
    if cart_item:
        db.delete(cart_item)
        db.commit()

    return RedirectResponse(url="/cart", status_code=303)


# ---------------------------------------------------
# PAGAR Y DESCONTAR STOCK
# ---------------------------------------------------
def pay_cart(request, db: Session):
    user = request.state.user
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    cart_items = db.query(CartItem).filter(CartItem.user_id == user.id_user).all()

    for item in cart_items:
        book = db.query(Book).filter(Book.id == item.book_id).first()
        if book and book.stock >= item.quantity:
            book.stock -= item.quantity
            db.delete(item)

    db.commit()
    return RedirectResponse(url="/books", status_code=303)
