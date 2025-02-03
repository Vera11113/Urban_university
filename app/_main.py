from fastapi import FastAPI
from routers import user, task
import uvicorn

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Welcome to Taskmaker!'}

app.include_router(task.task)
app.include_router(user.user)


