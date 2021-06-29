from sqlalchemy import Column, Integer, String, ForeignKey, TIME
from post.database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), default=1)
    creator = relationship("User", back_populates="posts")


class Stat(Base):
    __tablename__ = 'stats'
    id = Column(String, primary_key=True)
    average_run_time = Column(TIME())
    request_count = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    posts = relationship("Post", back_populates="creator")
