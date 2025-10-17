from fastapi import Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.books import Book

templates = Jinja2Templates(directory="views")

def get_home(request: Request, db: Session):
    libros = db.query(Book).limit(5).all()
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "libros": libros}
    )

# Para que la ruta sepa qué tipo de respuesta usa
get_home.response_class = HTMLResponse
