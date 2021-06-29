from fastapi import FastAPI
import models
from database import engine


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