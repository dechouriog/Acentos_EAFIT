from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import home_routes, books_routes, auth_routes
from utils.auth import get_current_user
from db.config import Base, engine

app = FastAPI()

# Configuración de las vistas
templates = Jinja2Templates(directory="views")

# Middleware: resuelve el usuario por request y lo deja en request.state.user
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def add_current_user(request: Request, call_next):
    request.state.user = get_current_user(request)  # objeto User o None
    response = await call_next(request)
    return response

# Rutas
app.include_router(home_routes.router)
app.include_router(books_routes.router)
app.include_router(auth_routes.router)

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
