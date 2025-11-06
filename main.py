from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import home_routes, books_routes, auth_routes, cart_routes, clima_routes
from utils.auth import get_current_user
from db.config import Base, engine

app = FastAPI()

# Configuración de las vistas
templates = Jinja2Templates(directory="views")


# --- ⚙️ Crear las tablas ---
@app.on_event("startup")
def on_startup():
    # ✅ Importa los modelos completos para que SQLAlchemy los registre
    import models.user  # Modelo de usuarios
    import models.books  # Modelo de libros
    import models.cart  # Modelo del carrito

    # ✅ Ahora sí, crea las tablas
    Base.metadata.create_all(bind=engine)


# --- 👤 Middleware de usuario ---
@app.middleware("http")
async def add_current_user(request: Request, call_next):
    request.state.user = get_current_user(request)
    response = await call_next(request)
    return response


# --- 🔗 Rutas ---
app.include_router(home_routes.router)
app.include_router(books_routes.router)
app.include_router(auth_routes.router)
app.include_router(cart_routes.router)
app.include_router(clima_routes.router)


# --- 🖼️ Archivos estáticos ---
app.mount("/static", StaticFiles(directory="static"), name="static")
