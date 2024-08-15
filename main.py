import datetime
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
# from aiogram.types import Message
# from aiogram.utils import executor
import config

API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот aiogram 3. Отправь мне любое сообщение и я повторю его")

@dp.message(F.text == 'Время')
@dp.message(Command("time"))
async def command_start(message: types.Message):
    myTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
    await message.answer("Текущее время:" + myTime)

@dp.message(F.text == 'Информация')
@dp.message(Command("info"))
async def command_start(message: types.Message):
    await message.answer("Бот по имени KamilBot")

@dp.message(Command("user"))
async def command_start(message: types.Message):
    thisUser = message.from_user.full_name
    await message.answer(f"Пользователь: {thisUser}")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
