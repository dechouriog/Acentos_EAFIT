from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes import home_routes, books_routes, auth_routes

app = FastAPI()

# Configuración de las vistas
templates = Jinja2Templates(directory="views")

# Rutas
app.include_router(home_routes.router)
app.include_router(books_routes.router)
app.include_router(auth_routes.router)

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
