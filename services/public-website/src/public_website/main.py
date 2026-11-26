from fastapi import FastAPI

app = FastAPI(title="Public Website")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}