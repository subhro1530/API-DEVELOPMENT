from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app= FastAPI()


# Basemodel checks if not empty any field
# If any field is empty it throws error
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None


# Declaring the decorator @ Symbol
@app.get("/")   

async def root():
    return {"message":"This is my api development tutorial!!!"}


@app.get("/posts")
def get_posts():
    return {"data":"This is your posts"}

# @app.post("/createposts")
# def create_posts(payload:dict=Body(...)):
#     print(payload)
#     return {"new_post":f"title {payload['title']} , content: {payload['content']}"}


@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.dict())
    return {"data":new_post}    #ending back the dictionary