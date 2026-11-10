from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Local RAG API")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Local RAG Backend API!"}

@app.post("/search")
def search_endpoint(request: QueryRequest):
    return {"query": request.query, "result": "API connection successful!"}