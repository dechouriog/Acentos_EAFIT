from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from db.config import get_db
from controllers.home_controller import get_home

router = APIRouter()

@router.get("/", response_class=get_home.response_class)
def home(request: Request, db: Session = Depends(get_db)):
    return get_home(request, db)
