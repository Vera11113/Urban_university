from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import StatesGroup, State
from numpy.ma.core import resize
from api import api
from keyboards import start_kb, kbi, kbi_buy
from glob import glob
import sqlite3



def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

def description(product):
    return f'Название: {product[1]} | Описание: {product[2]}  | Цена: {product[3]} '



api = api
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

images = glob(r"*.png")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_com(message):
    await message.answer("Привет! Выбери чем хочешь заняться: ", reply_markup=start_kb)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=kbi)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    products = get_all_products()
    for i in range(len(images)):
        with open(images[i], 'rb') as img:
            await message.answer_photo(img, description(products[i]))
    await message.answer(text = 'Выберите продукт: ', reply_markup=kbi_buy)


@dp.callback_query_handler(text = 'formulas')
async def form_print(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer(f'Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) + 5 * float(data['age']) - 161
    await message.answer(f'Ваша норма калорий {round(calories, 2)}')
    await state.finish()

@dp.callback_query_handler(text = 'product_buying')
async def product_buying(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text = 'Информация')
async def info_def(message):
    await message.answer('Этот бот считает норму калорий')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)