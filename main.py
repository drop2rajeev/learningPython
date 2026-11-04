
from fastapi import FastAPI

app = FastAPI(
    title="My Python API",
    description="Simple Python REST API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": True,
        "message": "Python API is working successfully"
    }

@app.get("/api/python/users")
def get_users():
    return {
        "status": True,
        "message": "Users API working successfully",
        "data": [
            {
                "id": 1,
                "name": "Rahul"
            },
            {
                "id": 2,
                "name": "Amit"
            }
        ]
    }

@app.get("/api/python/users/{user_id}")
def get_user(user_id: int):
    return {
        "status": True,
        "message": "User details fetched successfully",
        "data": {
            "id": user_id,
            "name": "Demo User"
        }
    }
