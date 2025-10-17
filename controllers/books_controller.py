from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models.books import Book

templates = Jinja2Templates(directory="views")

# LISTAR
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.books import Book

templates = Jinja2Templates(directory="views")


def list_books(request: Request, db: Session, page: int = 1, q: str = None, limit: int = 20):
    query = db.query(Book)

    # 🔍 Filtro por búsqueda
    if q:
        query = query.filter(
            or_(
                Book.title.ilike(f"%{q}%"),
                Book.author.ilike(f"%{q}%")
            )
        )

    total = query.count()  # total de resultados
    libros = query.offset((page - 1) * limit).limit(limit).all()

    return templates.TemplateResponse(
        "books/list.html",
        {
            "request": request,
            "libros": libros,
            "page": page,
            "total": total,
            "limit": limit,
            "q": q or ""
        }
    )

# CREAR (GET form / POST save)
def create_book_form(request: Request):
    return templates.TemplateResponse("books/create.html", {"request": request})

def create_book(request: Request, db: Session, data: dict):
    book = Book(**data)
    db.add(book)
    db.commit()
    db.refresh(book)
    return RedirectResponse(url="/books", status_code=303)

# LEER
def book_detail(request: Request, db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return HTMLResponse(content="Libro no encontrado", status_code=404)
    return templates.TemplateResponse("books/detail.html", {"request": request, "book": book})

# EDITAR
def edit_book_form(request: Request, db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return templates.TemplateResponse("books/edit.html", {"request": request, "book": book})

def update_book(db: Session, book_id: int, data: dict):
    book = db.query(Book).filter(Book.id == book_id).first()
    for key, value in data.items():
        setattr(book, key, value)
    db.commit()
    return RedirectResponse(url="/books", status_code=303)

# ELIMINAR
def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return RedirectResponse(url="/books", status_code=303)
