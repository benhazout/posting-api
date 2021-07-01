from pydantic import BaseModel, ValidationError, validator
from typing import List, Optional


# post schemas
class PostBase(BaseModel):
    title: str
    body: str


class Post(PostBase):
    class Config:
        orm_mode = True


class RequiredPosts(BaseModel):
    start: int
    limit: int

    @validator('limit')
    def must_be_larger_than_start(cls, v, values, **kwargs):
        if 'start' in values and v <= values['start']:
            raise ValueError('limit must be larger than start')
        return v


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
