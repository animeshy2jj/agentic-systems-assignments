from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/search")
def search(name: Optional[str] = None, age: Optional[int] = None):
    return {"name": name, "age": age}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
