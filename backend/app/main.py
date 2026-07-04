from fastapi import FastAPI

app = FastAPI(
    title="Rohan AI OS",
    description="Autonomous AI Operating System",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Rohan AI OS 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }