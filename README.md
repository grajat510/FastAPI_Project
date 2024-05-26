# FastAPI GitHub Repository Fetcher and Saver

This project is a FastAPI application that interacts with the GitHub API to fetch repository details and save them to a MongoDB database. It provides endpoints to fetch repository details directly from GitHub, save them to a MongoDB collection, and retrieve the saved repository details.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests
- PyMongo
- MongoDB

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name


2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies
pip install fastapi uvicorn requests pymongo

4. Ensure MongoDB is running
Make sure you have MongoDB installed and running on your machine. The default connection string is mongodb://localhost:27017/.

5. Running the Application
Start the FastAPI application
uvicorn github_api_app:app --reload

6. Access the API documentation
Open your web browser and go to http://127.0.0.1:8000/docs to see the interactive API documentation provided by Swagger UI.

7. API Endpoints

## Fetch Repository Details from GitHub
Endpoint: /repositories/{owner}/{repo}
Method: GET
Description: Fetches the details of a GitHub repository.

## Save Repository Details to MongoDB
Endpoint: /repositories/{owner}/{repo}/save
Method: POST
Description: Fetches the details of a GitHub repository and saves them to MongoDB.

## Fetch Saved Repository Details from MongoDB
Endpoint: /repositories
Method: GET
Description: Retrieves all saved repository details from MongoDB.

## Example Usage

1. Fetch a repository
curl -X GET "http://127.0.0.1:8000/repositories/owner-name/repo-name"

2. Save a repository
curl -X POST "http://127.0.0.1:8000/repositories/owner-name/repo-name/save"

3. Get all saved repositories
curl -X GET "http://127.0.0.1:8000/repositories"