from fastapi import FastAPI
from pymongo import MongoClient
from typing import List, Dict

app = FastAPI()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['jsonplaceholder']

@app.get("/posts")
async def get_posts():
    posts = list(db.posts.find({}, {'_id': False}))  # Exclude MongoDB's _id field
    return {"posts": posts}

@app.get("/comments")
async def get_comments():
    comments = list(db.comments.find({}, {'_id': False}))
    return {"comments": comments}

@app.get("/users")
async def get_users():
    users = list(db.users.find({}, {'_id': False}))
    return {"users": users}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app! Use /posts, /comments, or /users to get data."}
