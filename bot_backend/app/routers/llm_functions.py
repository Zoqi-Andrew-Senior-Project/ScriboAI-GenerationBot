from fastapi import APIRouter
import ollama
from pydantic import BaseModel

router = APIRouter()


class Prompt(BaseModel):
    text: str


@router.get("/api/generate", tags=["api"])
async def generate(request: Prompt):
    response = ollama.generate(model="llama3.2", prompt=request.text)
    return {"response": response["response"]}
