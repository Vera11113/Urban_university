from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


products = []
for i in range(1, 5):
    products.append(f'Название: Product{i}|Описание: описание {i}|Цена: {i}*100')


start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text = 'Рассчитать'),
        KeyboardButton(text = 'Информация'),
        KeyboardButton(text = 'Купить')
            ]
    ],
    resize_keyboard=True
)


kbi = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text = 'Формулы расчета', callback_data='formulas')]
    ]
)

kbi_buy = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text = 'Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text = 'Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text = 'Product4', callback_data='product_buying')]
    ]
)



