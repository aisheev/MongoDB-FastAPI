from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['jsonplaceholder']

# Pydantic Models
class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict

@app.get("/posts")
async def get_posts():
    posts = list(db.posts.find({}, {'_id': False}))
    return {"posts": posts}

@app.post("/posts", response_model=Post)
async def add_post(post: Post):
    result = db.posts.insert_one(post.dict())
    if result.acknowledged:
        return post
    raise HTTPException(status_code=500, detail="Failed to insert post")

@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    result = db.posts.update_one({'id': post_id}, {'$set': post.dict()})
    if result.matched_count:
        return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}", response_model=Dict[str, str])
async def delete_post(post_id: int):
    result = db.posts.delete_one({'id': post_id})
    if result.deleted_count:
        return {"detail": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/comments")
async def get_comments():
    comments = list(db.comments.find({}, {'_id': False}))
    return {"comments": comments}

@app.post("/comments", response_model=Comment)
async def add_comment(comment: Comment):
    result = db.comments.insert_one(comment.dict())
    if result.acknowledged:
        return comment
    raise HTTPException(status_code=500, detail="Failed to insert comment")

@app.put("/comments/{comment_id}", response_model=Comment)
async def update_comment(comment_id: int, comment: Comment):
    result = db.comments.update_one({'id': comment_id}, {'$set': comment.dict()})
    if result.matched_count:
        return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/comments/{comment_id}", response_model=Dict[str, str])
async def delete_comment(comment_id: int):
    result = db.comments.delete_one({'id': comment_id})
    if result.deleted_count:
        return {"detail": "Comment deleted"}
    raise HTTPException(status_code=404, detail="Comment not found")

@app.get("/users")
async def get_users():
    users = list(db.users.find({}, {'_id': False}))
    return {"users": users}

@app.post("/users", response_model=User)
async def add_user(user: User):
    result = db.users.insert_one(user.dict())
    if result.acknowledged:
        return user
    raise HTTPException(status_code=500, detail="Failed to insert user")

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    result = db.users.update_one({'id': user_id}, {'$set': user.dict()})
    if result.matched_count:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", response_model=Dict[str, str])
async def delete_user(user_id: int):
    result = db.users.delete_one({'id': user_id})
    if result.deleted_count:
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app! Use /posts, /comments, or /users to get data."}
