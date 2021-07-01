from .. import models, schemas
from sqlalchemy.orm import Session


def create(request: schemas.Post, db: Session):
    new_post = models.Post(title=request.title, body=request.body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def required(offset: int, limit: int, newest: bool, db: Session):
    if newest:
        posts = db.query(models.Post).order_by(models.Post.id.desc()).offset(offset).limit(limit).all()
        return posts
    posts = db.query(models.Post).offset(offset).limit(limit).all()
    return posts


def posts_number(db: Session):
    number_of_posts = db.query(models.Post).count()
    return number_of_posts
