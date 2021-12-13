from fastapi import FastAPI
from app.routes.student import route
from app.config.schedule import schedule_db
#, schedule_db1
app = FastAPI()

app.include_router(route)

@app.get('/')
async def do_something():
    return {"msg":"Hello world"}

schedule_db()
#schedule_db1()    
