from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from db.config import get_db
from controllers import books_controller

router = APIRouter(prefix="/books")

# LISTAR
@router.get("/")
def list_books(
    request: Request,
    db: Session = Depends(get_db),
    page: int = 1,
    q: str = None
):
    return books_controller.list_books(request, db, page, q)


# CREAR
@router.get("/create")
def create_form(request: Request):
    return books_controller.create_book_form(request)

@router.post("/create")
def create(request: Request,
           db: Session = Depends(get_db),
           isbn13: str = Form(...),
           author: str = Form(...),
           title: str = Form(...)):
    data = {"isbn13": isbn13, "author": author, "title": title}
    return books_controller.create_book(request, db, data)

# LEER
@router.get("/{book_id}")
def detail(request: Request, book_id: int, db: Session = Depends(get_db)):
    return books_controller.book_detail(request, db, book_id)

# EDITAR
@router.get("/edit/{book_id}")
def edit_form(request: Request, book_id: int, db: Session = Depends(get_db)):
    return books_controller.edit_book_form(request, db, book_id)

@router.post("/edit/{book_id}")
def edit(book_id: int,
         db: Session = Depends(get_db),
         isbn13: str = Form(...),
         author: str = Form(...),
         title: str = Form(...)):
    data = {"isbn13": isbn13, "author": author, "title": title}
    return books_controller.update_book(db, book_id, data)

# ELIMINAR
@router.post("/delete/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    return books_controller.delete_book(db, book_id)
