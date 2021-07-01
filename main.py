from fastapi import FastAPI
from post import models
from post.database import engine
from post.routers import user, authentication, posts


tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Post",
        "description": "Manage posts. ",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

# when we find any data in the models create tables
models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(posts.router_post)
app.include_router(posts.router_posts)
app.include_router(posts.router_postsnumber)
