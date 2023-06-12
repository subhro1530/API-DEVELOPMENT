from random import randrange
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


# Database 1
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}]


# Declaring the decorator @ Symbol
@app.get("/")   

async def root():
    return {"message":"This is my api development tutorial!!!"}


# @app.get("/posts")
# def get_posts():
#     return {"data":"This is your posts"}

# @app.post("/createposts")
# def create_posts(payload:dict=Body(...)):
#     print(payload)
#     return {"new_post":f"title {payload['title']} , content: {payload['content']}"}


# @app.post("/createposts")
# def create_posts(new_post:Post):
#     print(new_post.dict())
#     return {"data":new_post}    #ending back the dictionary


# Database return
@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/createposts")
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    return{"data":post_dict}

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
    
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int):
    post=find_post(id) # Convert String to int
    print(post)
    return {"post detail":post}