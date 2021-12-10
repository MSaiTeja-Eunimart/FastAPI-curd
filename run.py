from fastapi import FastAPI
from app.routes.student import route

app = FastAPI()

app.include_router(route)

@app.get('/')
def do_something():
    return {"msg":"Hello world"}
    
