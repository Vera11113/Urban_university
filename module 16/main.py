from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {'message': 'Главная страница'}

@app.get("/user/admin")
async def admin_enter() ->dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def user_name(user_id) -> dict:
    return {'message': f'Вы вошли как пользователь №{user_id}'}


@app.get("/user")
async def get_name(username:str, age:int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст {age}'}
