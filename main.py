from fastapi import FastAPI
from post import models
from post.database import engine
from post.routers import user, authentication, posts


tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users: create users ([POST/user] and get user data by id ([GET/user/{id}]))",
    },
    {
        "name": "Posts",
        "description": "Operations with users: get required posts - using offset (where to start from), limit (the "
                       "amount of posts) and newest (true or false - bring posts from newest created or not)",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

# when we find any data in the models create tables
models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(posts.router_posts)
app.include_router(posts.router_postsnumber)
