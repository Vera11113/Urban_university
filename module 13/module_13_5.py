from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import StatesGroup, State
from numpy.ma.core import resize

from api import api
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from task import button

api = api
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button1 = KeyboardButton(text = 'Рассчитать')
kb.insert(button1)
button2 = KeyboardButton(text = 'Информация')
kb.insert(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_com(message):
    await message.answer("Привет! Выбери чем хочешь заняться: ", reply_markup=kb)


@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer(f'Введите свой возраст:')
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)