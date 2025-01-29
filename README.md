# HNG12 Backend API Task

This is a simple public API for the HNG12 Internship.

## Features
- Returns email, current datetime in ISO 8601, and a GitHub link.
- Supports CORS.
- Deployed with Render.

## installation and setup
1. # clone the repository
```bash
git clone https://github.com/Khiingleo/hng12-backend-api-task.git
cd hng12-backend-api-task.git
```
2. # Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. # install dependencies
```bash
pip install requirements.txt
```

4. # Run locally
```bash
python3 app.py
```
* this will run on http://localhost:5000/api

## API Documentation
# Base URL
https://hng12-backend-api-task.git.onrender.com



## Endpoint
### `GET /api`
#### Response:
```json
{
  "email": "shalomzymike@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Khiingleo/hng12-backend-api-task"
}


## Backlink  
[Hire Python Developers](https://hng.tech/hire/python-developers)