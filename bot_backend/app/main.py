from fastapi import FastAPI
from pydantic import BaseModel

class Prompt(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": " Hello Scribo"}

@app.get("/api/generate/")
def generate_script(prompt: Prompt):
    return {"response": prompt}
