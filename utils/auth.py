from fastapi import Request, Response
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "mi_secreto_super_seguro"
ALGORITHM = "HS256"

# --- Crear token JWT ---
def create_token(username: str):
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": username, "exp": expire}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# --- Leer token y devolver usuario ---
def get_current_user(request: Request):
    token = request.cookies.get("token")
    if not token:
        return None
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")  # devuelve el username
    except jwt.ExpiredSignatureError:
        return None
    except jwt.PyJWTError:
        return None

# --- Setear cookie ---
def set_token_cookie(response: Response, token: str):
    response.set_cookie(key="token", value=token, httponly=True)

# --- Limpiar cookie ---
def clear_token_cookie(response: Response):
    response.delete_cookie(key="token")
