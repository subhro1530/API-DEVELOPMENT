# API Development

## FastAPI

> [Documentation](https://fastapi.tiangolo.com/tutorial/first-steps/)

## Steps to be followed.

1.  Check for python version

```bash
python --version
```

2.  Create a virtual enviornment (python)

```bash
python -m venv <name>
```

3.  Read the FastAPI docs for problems.
    [link](https://fastapi.tiangolo.com/tutorial/)

4.  Switch the command palette default run engine from global python to the python.exe file of the virtual enviornment created.

5.  Run to install FastAPI:

```bash
pip install "fastapi[all]"
```

Start the process(host):

```bash
uvicorn main:app --reload
```

## GET Request

6.  Test the execution of the code

```python


from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


```

7.  Run:

```bash


(VirtualEnv) D:\Desktop\API DEVELOPMENT>uvicorn main:app
INFO:     Started server process [30124]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


```

8.  Result in the browser:

```JSON

message:	"Hello World"

```

9.  To make changes and then reload:

```bash

(VirtualEnv) D:\Desktop\API DEVELOPMENT>uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\Desktop\\API DEVELOPMENT']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28548] using WatchFiles
INFO:     Started server process [10992]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

10. Adding a '/posts' and then Fetching the data:

```python

from fastapi import FastAPI

app= FastAPI()

# Declaring the decorator @ Symbol
@app.get("/")

async def root():
    return {"message":"This is my api development tutorial!!!"}


@app.get("/posts")
def get_posts():
    return {"data":"This is your posts"}

```

```powershell

(VirtualEnv) PS D:\Desktop\API DEVELOPMENT> uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\Desktop\\API DEVELOPMENT']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [31612] using WatchFiles
INFO:     Started server process [16308]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:49290 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:49297 - "GET /postss HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:49298 - "GET /posts HTTP/1.1" 200 OK

```

## Post Request

11. Syntax:

```python


@app.post("/createposts")
def create_posts():
    return {"message":"Successfully created the post."}

```

12. Insert a payload from the postman body and print it in conssole

```python
from fastapi.params import Body

@app.post("/createposts")
def create_posts(payload:dict=Body(...)):
    print(payload)
    return {"message":"Successfully created the post."}

```

13. Make the payload content return as a dictionary:

```python
@app.post("/createposts")
def create_posts(payload:dict=Body(...)):
    print(payload)
    return {"new_post":f"title {payload['title']} , content: {payload['content']}"}

```

## Using new library: Pydantic

1.

```python
from pydantic import BaseModel

# Basemodel checks if not empty any field
# If any field is empty it throws error
class Post(BaseModel):
    title:str
    content:str

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.title)
    return {"data":"new post"}

```

2.  Implementing some boolean logic to check:

```python

# Basemodel checks if not empty any field
# If any field is empty it throws error
class Post(BaseModel):
    title:str
    content:str
    published:bool=True


@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.published)
    return {"data":"new post"}

```

```bash
INFO:     Application startup complete.
True
INFO:     127.0.0.1:51110 - "POST /createposts HTTP/1.1" 200 OK
```

3.  Implement an optional field

```python
from typing import Optional

# Basemodel checks if not empty any field
# If any field is empty it throws error
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

```

```bash
INFO:     Application startup complete.
None
INFO:     127.0.0.1:51201 - "POST /createposts HTTP/1.1" 200 OK
```

4.  Printing the rating after changing it in postman:

```python
@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post)
    print(new_post.rating)
    return {"data":"new post"}
```

```bash
INFO:     127.0.0.1:51201 - "POST /createposts HTTP/1.1" 200 OK
INFO:     127.0.0.1:51228 - "POST /createposts HTTP/1.1" 422 Unprocessable Entity
4
INFO:     127.0.0.1:51252 - "POST /createposts HTTP/1.1" 200 OK
```

5.  On printing the new_post as .dict() method converts the post into a dictionary.

```python
@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.dict())
    return {"data":"new post"}

```

```bash
{'title': 'top beaches in india', 'content': 'Reasults of beaches are being fetched...', 'published': True, 'rating': 4}
```

6. Sending the new post to postman by returning it:

```python
@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.dict())
    return {"data":new_post}    #ending back the dictionary
```

```JSON
{
    "data": {
        "title": "top beaches in india",
        "content": "Reasults of beaches are being fetched...",
        "published": true,
        "rating": 4
    }
}
```

## Creating database and fetching from it:

1.

```python
# Database 1
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}]

# Database return
@app.get("/posts")
def get_posts():
    return {"data":my_posts}
```

Recieved From Postman:

```JSON
{
    "data": [
        {
            "title": "title of post 1",
            "content": "content of post 1",
            "id": 1
        },
        {
            "title": "title of post 2",
            "content": "content of post 2",
            "id": 2
        }
    ]
}
```

2. Giving a random id to the post function while anything is posted and then returning it. Also merging with the get method 'my_posts' variable. Dynamically adding to the database created :

```python
# Created Previously
# Basemodel checks if not empty any field
# If any field is empty it throws error
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

# Database 1
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}]

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

```

### POST Request

```JSON
{
    "data": {
        "title": "top beaches in india",
        "content": "Reasults of beaches are being fetched...",
        "published": true,
        "rating": 4,
        "id": 17030385
    }
}
```

### GET Request

```JSON
{
    "data": [
        {
            "title": "title of post 1",
            "content": "content of post 1",
            "id": 1
        },
        {
            "title": "title of post 2",
            "content": "content of post 2",
            "id": 2
        },
        {
            "title": "top beaches in india",
            "content": "Reasults of beaches are being fetched...",
            "published": true,
            "rating": 4,
            "id": 17030385
        },
        {
            "title": "top beaches in india",
            "content": "Reasults of beaches are being fetched...",
            "published": true,
            "rating": 4,
            "id": 56611228
        }
    ]
}
```

3.  Retrieving one indivitual post:

```python
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id):
    print(id)
    return {"post detail":f"Here is post {id}"}
```

### GET method

```
http://127.0.0.1:8000/posts/2
```

```JSON
{
    "post detail": "Here is post 2"
}
```

4. Searching through the id's

```python
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id):
    post=find_post(id)
    return {"post detail":post}
```

```JSON
{
    "post detail": null
}
```

Wrong Output since the id type is int but the given id is string. This is why the search result is null.

Correction:

```python
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id):
    post=find_post(int(id)) # Convert String to int
    print(post)
    return {"post detail":post}
```

```JSON
{
    "post detail": {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    }
}
```

4. To validate the id:

```python
def get_post(id:int):   # This will make sure it is always converted
    post=find_post(id) # Now we dont need to convert
    print(post)
    return {"post detail":post}
```

```JSON
{
    "post detail": {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    }
}
```

5. To know that order of writing code maatters :

```python
#This code will throw an error while get request since the id parameter would be instantiated with 'latest' and it will be a type mismatch...
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int):
    post=find_post(id) # Convert String to int
    print(post)
    return {"post detail":post}


@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"Latest Post":post}
```

Correction:

```python
#This is how order o execution matters and this code will execute the /latest first and the /{id} later throwing no error.
@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int):
    post=find_post(id) # Convert String to int
    print(post)
    return {"post detail":post}


@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"Latest Post":post}
```

6.  To manipulate the error response code i.e to return 404 error if not found:

```python

from fastapi import FastAPI,Response    # Response added

@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int,response:Response):
    post=find_post(id) # Convert String to int
    if not post:    # If post contains a null value
        response.status_code=404
    print(post)
    return {"post detail":post}
```

Also another way:

```python
from fastapi import FastAPI,Response, status

@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int,response:Response):
    post=find_post(id) # Convert String to int
    if not post:    # If post contains a null value
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'message':f"post with {id} was not found."}
    print(post)
    return {"post detail":post}

```

In one line:

```python
from fastapi import FastAPI,Response, status,HTTPException

@app.get("/posts/{id}")     # This id is path parameter
def get_post(id:int):
    post=find_post(id) # Convert String to int
    if not post:    # If post contains a null value
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} was not found.")
    return {"post detail":post}
```

7.  To manipulate the post >> 201_Created

```python
@app.post("/createposts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    return{"data":post_dict}
```

### Deleting Posts

1.  Deleting posts:

```python
# Deleting Posts
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i


@app.delete("/posts/{id}")
def delete_post(id:int):
    #   deleting post
    #   find the index in the array that has required ID
    #   my_posts.pop(index)
    index=find_index_post(id)

    my_posts.pop(index)
    return {"message":"Post was successfully deleted."}
```

2. Another way with HTTPException:

```python
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
```

### Update post

1.  Creating the layout:

```python

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    index=find_index_post(id)

    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"post with id:{id} doesnot exist.")

    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict


    return {'data':post_dict}

```

2.  Slight change from the docs:

> Create a folder known as app
> Create a **init**.py file
> Inside this file:

```python

```

```bash
(VirtualEnv) D:\Desktop\API DEVELOPMENT>cd app

(VirtualEnv) D:\Desktop\API DEVELOPMENT\app>uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\Desktop\\API DEVELOPMENT\\app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [26020] using WatchFiles
INFO:     Started server process [35312]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

### To create the database and other installs:

[Start : 2:44:00](https://youtu.be/0sOvCWFmrtA?t=9876)

### Some Queries in SQl

SELECT

```SQL

SELECT * from products;
```

```SQL
SELECT * from products WHERE is_sale=True;
```

```SQL
SELECT id,price from products where is_sale=True;
```

```SQL
SELECT * from products where price>=50;
```

```SQL
SELECT * from products where is_sale!=False;
```

```SQL
SELECT * from products where id>2 AND inventory>=6 AND price >=50;

```

```SQL
SELECT * from products WHERE name LIKE 'TV%';
```

```SQL
SELECT * from products WHERE name LIKE '%e';
```

```SQL
SELECT * from products ORDER BY price ASC;
```

```SQL
SELECT * from products ORDER BY price DESC;
```

```SQL
SELECT * from products ORDER BY price DESC;
```

INSERT

```SQL
INSERT INTO products (id,price,name,inventory) VALUES (104,45,'USA',1);
SELECT * from products WHERE name='tortilla'
```

DELETE

```SQL
DELETE FROM products WHERE id=101;
```

```SQL
DELETE FROM products WHERE id=101;

DELETE FROM products WHERE id=102 RETURNING *;

DELETE FROM products WHERE inventory=0;
SELECT * FROM products

```

UPDATE

```SQL
UPDATE products SET name='Flower' , price=4 WHERE id=144

UPDATE products SET name='Flower' , price=4,is_sale=true WHERE id=104;
SELECT * FROM products;

UPDATE products SET is_sale=true WHERE id>100;
SELECT * FROM products;
```

## Installing and working with psycopg2, a link between python and the database

```bash
(VirtualEnv) D:\Desktop\API DEVELOPMENT>pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.6-cp310-cp310-win_amd64.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 186.1 kB/s eta 0:00:00
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.6
```

Code to establish the connection:

```python
import psycopg2

#   Establishing Connection
try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='*********',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Database connection was successful.")
except Exception as error:
    print("Connecting to the database failed.")
    print("Error: ",error)
```

Code to continue the connection calls till it is successful:

```python
#   Establishing Connection
while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='********',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successful.")
        break
    except Exception as error:
        print("Connecting to the database failed.")
        print("Error: ",error)
        sleep(2)
```

## Creating new HTTPRequests with SQL Queries

```python

# Database return
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    print(posts)
    return {"data":my_posts}

```

```bash
Database connection was successful.
INFO:     Started server process [26260]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
[RealDictRow([('id', 2), ('title', 'first post'), ('content', 'This is my first post.\n'), ('published', True), ('created_at', datetime.datetime(2023, 6, 16, 20, 44, 18, 918841, tzinfo=datetime.timezone(datetime.timedelta(seconds=19800))))]), RealDictRow([('id', 3), ('title', 'second post\n'), ('content', 'This is my second post.'), ('published', False), ('created_at', datetime.datetime(2023, 6, 16, 20, 44, 18, 918841, tzinfo=datetime.timezone(datetime.timedelta(seconds=19800))))])]
```

To Get the sql server

```sql

```

```JSON
{
    "data": [
        {
            "id": 2,
            "title": "first post",
            "content": "This is my first post.\n",
            "published": true,
            "created_at": "2023-06-16T20:44:18.918841+05:30"
        },
        {
            "id": 3,
            "title": "second post\n",
            "content": "This is my second post.",
            "published": false,
            "created_at": "2023-06-16T20:44:18.918841+05:30"
        }
    ]
}
```
