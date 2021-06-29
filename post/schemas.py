from pydantic import BaseModel
from typing import List, Optional


# post schemas
class PostBase(BaseModel):
    title: str
    body: str


class Post(PostBase):
    class Config:
        orm_mode = True


# user schema
class User(BaseModel):
    name: str
    username: str
    password: str


# show schemas
class ShowUserBase(BaseModel):
    name: str
    username: str

    class Config:
        orm_mode = True


class ShowUser(ShowUserBase):
    posts: List[Post] = []


class ShowPost(BaseModel):
    title: str
    body: str
    creator: ShowUserBase

    class Config:
        orm_mode = True


# login schema
class Login(BaseModel):
    username: str
    password: str


# token schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
