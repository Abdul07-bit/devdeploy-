from fastapi import FastAPI

app = FastAPI(
    title="DevDeploy",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "DevDeploy",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/users")
def users():
    return {
        "users": [
            {"id": 1, "name": "Abdul"},
            {"id": 2, "name": "DevOps User"}
        ]
    }
