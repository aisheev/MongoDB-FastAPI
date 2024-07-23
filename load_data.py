import requests
from pymongo import MongoClient

# Retrieve data from API
posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')
users_response = requests.get('https://jsonplaceholder.typicode.com/users')

posts = posts_response.json()
comments = comments_response.json()
users = users_response.json()

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['jsonplaceholder']

# Insert data into MongoDB
db.posts.insert_many(posts)
db.comments.insert_many(comments)
db.users.insert_many(users)
