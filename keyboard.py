from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start'),KeyboardButton(text='/info')],
        # [KeyboardButton(text='/info')],
        # [KeyboardButton(text='/time')],
        [KeyboardButton(text='/time'),KeyboardButton(text='/user')]
    ],
    resize_keyboard=True
)