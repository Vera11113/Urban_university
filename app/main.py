from fastapi import FastAPI
from routers import user, task

app = FastAPI()

@app.get('/')
async def start()->dict:
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.task)
app.include_router(user.user)