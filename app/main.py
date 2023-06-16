from random import randrange
from time import sleep
from typing import Optional
from fastapi import FastAPI,Response, status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app= FastAPI()


# Basemodel checks if not empty any field
# If any field is empty it throws error
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None


#   Establishing Connection
while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='saha@2004',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successful.")
        break
    except Exception as error:
        print("Connecting to the database failed.")
        print("Error: ",error)
        sleep(2)

# Database 1
# my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}]


# Declaring the decorator @ Symbol
# @app.get("/")   

# async def root():
#     return {"message":"This is my api development tutorial!!!"}


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


# New posts
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}]


# Database return
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    print(posts)
    return {"data":posts}



@app.post("/createposts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    return{"data":post_dict}

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
# @app.get("/posts/latest")
# def get_latest_post():
#     post=my_posts[len(my_posts)-1]
#     return{"Latest Post":post}
    
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int):
    post=find_post(id) # Convert String to int
    if not post:    # If post contains a null value
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} was not found.")
    return {"post detail":post}



# Deleting Posts
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #   deleting post
    #   find the index in the array that has required ID
    #   my_posts.pop(index)
    index=find_index_post(id)

    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"post with id:{id} doesnot exist.")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    index=find_index_post(id)

    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"post with id:{id} doesnot exist.")
    
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict

    
    return {'data':post_dict}
