from .. import models, schemas
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def create(request: schemas.User, db: Session):
    # check if username exists
    if db.query(models.User).filter(models.User.username == request.username).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'username {request.username} already taken')

    # save user to database
    new_user = models.User(name=request.name, username=request.username, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} was not found')
    return user
