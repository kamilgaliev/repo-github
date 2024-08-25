import datetime
from aiogram import Router, types, F
from aiogram.filters.command import Command
from second_bot.keyboards.keyboard import keyboard
from second_bot.utils.random_fox import random_fox
from random import randint

router = Router()

@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот aiogram 3. Отправь мне любое сообщение и я повторю его",reply_markup=keyboard)

@router.message(F.text.lower() == 'время')
@router.message(Command("time"))
async def command_start(message: types.Message):
    myTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
    await message.answer("Текущее время:" + myTime)

@router.message(F.text.lower() == 'информация')
@router.message(Command("info"))
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

@router.message(Command("user"))
async def command_start(message: types.Message):
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    await message.answer(f"Ваше полное имя: {full_name}")

@router.message(F.text.lower() == 'лиса')
@router.message(Command("fox"))
async def command_fox(message: types.Message):
    image_fox = random_fox()
    await message.answer_photo(photo=image_fox, reply_markup=keyboard)

@router.message(F.text.lower() == 'число')
@router.message(Command("number"))
async def command_random_int(message: types.Message):
    number = randint(1,10)
    await message.answer(f"{number}", reply_markup=keyboard)

@router.message()
async def echo(message: types.Message):
    await message.answer(message.text, reply_markup=keyboard)
