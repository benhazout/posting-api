from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
from ..services import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get(id, db)
