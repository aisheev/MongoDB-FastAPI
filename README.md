# Turbit-MongoDB-FastAPI
MongoDB and API Development Exercise


**Objective**

Develop a pipeline that involves setting up a MongoDB database using Docker Compose, retrieving and storing data from an external API, and exposing this data through FastAPI.

**Prerequisites**

Before you begin, ensure you have met the following requirements:

	•	Docker and Docker Compose installed on your local machine
	•	Python 3.7+ installed
	•	pip package manager


**Setup MongoDB with Docker Compose:**

1.	Clone the repository:
git clone <repository-url>
cd <repository-directory>

2.	Navigate to the directory containing the docker-compose.yml file and run Docker Compose:
   
docker-compose up -d

This will set up a MongoDB instance.

**Data Retrieval and Loading into MongoDB**

1. Install the required Python packages
2. Run the script to retrieve data from the external API and store it in MongoDB

   python load_data.py

   This script will fetch data from https://jsonplaceholder.typicode.com/ and store it in the MongoDB database.

**Create a RESTful API with FastAPI**

1. Start the FastAPI application:

    uvicorn main:app --reload

   This will start the FastAPI server on http://127.0.0.1:8000.

**Testing the API**

You can test the API using tools like Postman or curl. Alternatively, you can visit http://127.0.0.1:8000/docs to explore and test the API using the interactive Swagger UI provided by FastAPI.

