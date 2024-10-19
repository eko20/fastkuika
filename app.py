
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from typing import Union

app = FastAPI()

# Define a request body model using Pydantic
class QueryRequest(BaseModel):
    query: str
    


    
file_path = "C:\\Users\\mekin\\Desktop\\IPCC_AR6_WGII_Chapter03.pdf"



@app.post("/get-query")
async def get_query(request: QueryRequest):
    # Access the query from the request body
    return {"received_query": request.query,
            "lessonplan": "calişcan",
            "çabaliyican": "popkek severeim"
            }
