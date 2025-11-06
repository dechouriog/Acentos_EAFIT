from sqlalchemy.orm import Session
from fastapi import Response
from models.user import User
from db.config import SessionLocal
from utils.auth import create_token, set_token_cookie, clear_token_cookie
from werkzeug.security import generate_password_hash, check_password_hash

# --- Helpers de DB ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Registro ---
def handle_register(username: str, password: str, email: str, name: str, user_type="normal", address=None, phone_number=None):
    db = next(get_db())
    existing_user = db.query(User).filter((User.username == username) | (User.mail == email)).first()
    if existing_user:
        return False  

    hashed_pw = generate_password_hash(password)
    new_user = User(
        username=username,
        password=hashed_pw,
        mail=email,
        name=name,
        user_type=user_type,
        address=address,
        phone_number=phone_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return True

# --- Login ---
def handle_login(response: Response, username: str, password: str):
    db = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False

    if not check_password_hash(user.password, password):
        return False

    token = create_token(user.username)
    set_token_cookie(response, token)
    return True

# --- Logout ---
def handle_logout(response: Response):
    clear_token_cookie(response)
