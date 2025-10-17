from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers import auth_controller
from utils.auth import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="views")

# --- LOGIN PAGE ---
@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if get_current_user(request):
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request})

# --- LOGIN POST ---
@router.post("/login")
async def do_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if get_current_user(request):
        return RedirectResponse("/", status_code=303)

    response = RedirectResponse("/", status_code=303)
    success = auth_controller.handle_login(response, username, password)

    if not success:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Credenciales inválidas"})
    return response

# --- REGISTER PAGE ---
@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    if get_current_user(request):  # <-- verifica si ya hay usuario loggeado
        return RedirectResponse("/", status_code=303)  # <-- redirige al home
    return templates.TemplateResponse("register.html", {"request": request})

# --- REGISTER POST ---
@router.post("/register")
async def do_register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    name: str = Form(...)
):
    if get_current_user(request):  # <-- también evita que un usuario loggeado haga POST
        return RedirectResponse("/", status_code=303)

    success = auth_controller.handle_register(username, password, email, name)
    if success:
        return RedirectResponse("/login", status_code=303)
    return HTMLResponse("Usuario o correo ya existe", status_code=400)


# --- LOGOUT ---
@router.get("/logout")
async def logout():
    response = RedirectResponse("/", status_code=303)
    auth_controller.handle_logout(response)
    return response
