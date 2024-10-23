from fastapi import FastAPI
from .routers import llm_functions

app = FastAPI()

app.include_router(llm_functions.router)


@app.get("/")
def read_root():
    return {"message": " Hello Scribo"}
