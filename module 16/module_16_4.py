from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, List


app = FastAPI()

users = []

class User(BaseModel):
    id: int=None
    username: str = Field(min_length = 4, max_length = 20, description='Enter user name')
    age: int = Field(ge=18, le = 120, description='Enter user age')


@app.get("/")
async def start() -> str:
    return 'Welcome!'

@app.get("/users")
async def users_db() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username, age) -> User:
    user_id = len(users)+1
    new_user = User(id = user_id, username = username, age = age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username, age) -> User:
    try:
        user_info = users[user_id-1]
        user_info.username = username
        user_info.age = age
        return user_info
    except IndexError:
        raise HTTPException(status_code=404, detail = 'user was not found')



@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return f'User {user_id} is deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')





