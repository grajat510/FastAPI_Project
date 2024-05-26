from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId from bson module
import requests

# MongoDB connection settings
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
MONGO_DB_NAME = "github_data"
MONGO_COLLECTION_NAME = "repositories"

# GitHub API settings
GITHUB_API_URL = "https://api.github.com"

# Initialize FastAPI app
app = FastAPI()

# Initialize MongoDB client
mongo_client = MongoClient(MONGO_CONNECTION_STRING)
db = mongo_client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

# Route to fetch repository details from GitHub API
@app.get("/repositories/{owner}/{repo}")
async def get_repository(owner: str, repo: str):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        repository_data = response.json()
        return repository_data
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

# Route to save repository details to MongoDB
@app.post("/repositories/{owner}/{repo}/save")
async def save_repository(owner: str, repo: str):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        repository_data = response.json()
        # Save repository data to MongoDB
        collection.insert_one(repository_data)
        return {"message": "Repository details saved successfully"}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

# Route to fetch saved repository details from MongoDB
@app.get("/repositories")
async def get_saved_repositories():
    repositories = []
    for repo in collection.find():
        # Convert ObjectId to string and convert MongoDB document to dictionary
        repo['_id'] = str(repo['_id'])
        repositories.append(repo)
    return repositories

# Run FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
