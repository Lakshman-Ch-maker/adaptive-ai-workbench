from fastapi import FastAPI

app = FastAPI(
    title="Adaptive AI Workbench",
    description="Cloud-native adaptive multi-agent AI platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "Adaptive AI Workbench",
        "status": "Running",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }