
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a request body model using Pydantic
class QueryRequest(BaseModel):
    query: str

@app.post("/get-query")
async def get_query(request: QueryRequest):
    # Access the query from the request body
    return {"received_query": request.query}
