from fastapi import APIRouter, Depends, status, Query
from typing import List
from sqlalchemy.orm import Session
from .. import oauth2, schemas
from ..services import posts

from ..database import get_db

router_posts = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

router_postsnumber = APIRouter(
    prefix='/postsnumber',
    tags=['Posts']
)


@router_posts.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Post, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return posts.create(request, db)


@router_posts.get('/', response_model=List[schemas.ShowPost])
def required_posts(
        offset: int = Query(..., gt=-1),
        limit: int = Query(..., ),
        newest: bool = True,
        db: Session = Depends(get_db)
):
    return posts.required(offset, limit, newest, db)


@router_postsnumber.get('/')
def posts_number(db: Session = Depends(get_db)):
    return {'posts_number': posts.posts_number(db)}
