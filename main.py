from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
  author: str
  title: str
  content: str
  tags: Optional[str]= None
  

@app.get('/')
def index():
  return { "message": "Hey!" }

@app.get('/posts/{id}')
def getPost(id: int):
  return { "data": id }

@app.post('/posts')
def addPost(post: Post):
  return { "message": f"The post {post.title} has been added" }