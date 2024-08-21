import datetime
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.types import Message
# from aiogram.utils import executor
from keyboard import keyboard
import config

API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот aiogram 3. Отправь мне любое сообщение и я повторю его",reply_markup=keyboard)

@dp.message(F.text == 'Время')
@dp.message(Command("time"))
async def command_start(message: types.Message):
    myTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
    await message.answer("Текущее время:" + myTime)

@dp.message(F.text == 'Информация')
@dp.message(Command("info"))
async def command_start(message: types.Message):
    info_text = (
        "Я эхо-бот, созданный с использованием библиотеки aiogram.\n"
        "Я повторяю все, что вы мне пишете.\n"
        "Команды:\n"
        "/start - Приветственное сообщение\n"
        "/info - Информация о боте\n"
        "/time - Текущее время\n"
        "/user - Полное имя пользователя"
    )
    await message.answer(info_text, reply_markup=keyboard)

@dp.message(Command("user"))
async def command_start(message: types.Message):
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    await message.answer(f"Ваше полное имя: {full_name}")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text, reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
