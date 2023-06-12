# API Development

## FastAPI

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
